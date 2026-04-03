import { useParams, Link, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import Chatbot from "@/components/chatbot/Chatbot";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  ArrowLeft,
  Volume2,
  Check,
  FileText,
  ExternalLink,
  Calendar,
  Building2,
  Award,
  Languages,
  Tag,
} from "lucide-react";
import { cn } from "@/lib/utils";

interface Scheme {
  scheme_id: string;
  scheme_name: string;
  description: string;
  benefits: string[];
  eligibility: string[];
  required_documents: string[];
  ministry: string;
  deadline: string;
  officialUrl: string;
  sector: string;
  category?: string;
  matchScore?: number;
}

const SchemeDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [scheme, setScheme] = useState<Scheme | null>(null);
  const [loading, setLoading] = useState(true);

  /* ---------------- VOICE STATES ---------------- */

  const [isPlaying, setIsPlaying] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState("en");
  const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);

  /* ---------------- LOAD VOICES ---------------- */

  useEffect(() => {
    const synth = window.speechSynthesis;

    const loadVoices = () => {
      const voiceList = synth.getVoices();
      setVoices(voiceList);
    };

    loadVoices();

    if (synth.onvoiceschanged !== undefined) {
      synth.onvoiceschanged = loadVoices;
    }
  }, []);

  /* ---------------- FETCH SCHEME ---------------- */

  useEffect(() => {
    const fetchScheme = async () => {
      try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/scheme/${id}`);

        if (!res.ok) {
          throw new Error("Scheme API error");
        }

        const data = await res.json();
        console.log("Scheme API response:", data);

        let schemeData = data.scheme ? data.scheme : data;

        const normalizeField = (field: any): string[] => {
          if (!field) return [];

          if (Array.isArray(field)) {
            return field.map((item) =>
              typeof item === "object"
                ? Object.entries(item)
                    .map(([k, v]) => `${k.replace("_", " ")}: ${v}`)
                    .join(", ")
                : String(item)
            );
          }

          if (typeof field === "object") {
            return Object.entries(field).map(
              ([k, v]) => `${k.replace("_", " ")}: ${v}`
            );
          }

          return [String(field)];
        };

        schemeData = {
          ...schemeData,
          benefits: normalizeField(schemeData.benefits || schemeData.benefit),
          eligibility: normalizeField(
            schemeData.eligibility || schemeData.eligibility_criteria
          ),
          required_documents: normalizeField(
            schemeData.required_documents ||
              schemeData.requiredDocuments ||
              schemeData.documents
          ),
        };

        setScheme(schemeData);
        setLoading(false);
      } catch (error) {
        console.error("Error loading scheme:", error);
        setLoading(false);
      }
    };

    if (id) {
      fetchScheme();
    }
  }, [id]);

  /* ---------------- VOICE ASSISTANCE ---------------- */

  // Map language code -> BCP-47 primary tag (used for strict voice matching)
  const LANG_CODES: Record<string, string> = {
    en: "en",
    hi: "hi",
    ml: "ml",
  };

  // Map language code -> canonical BCP-47 locale for the utterance
  const LANG_LOCALES: Record<string, string> = {
    en: "en-IN",
    hi: "hi-IN",
    ml: "ml-IN",
  };

  /**
   * Translate English text to the target language via Google Translate
   * (unofficial free endpoint). Returns the original text on failure.
   */
  const translateText = async (text: string, targetLang: string): Promise<string> => {
    try {
      const res = await fetch(
        `https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=${targetLang}&dt=t&q=${encodeURIComponent(text)}`
      );
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      // data[0] is an array of [translatedChunk, originalChunk] pairs
      if (!Array.isArray(data?.[0])) throw new Error("Unexpected response shape");
      return data[0].map((item: any) => item?.[0] ?? "").join("");
    } catch (err) {
      console.error("Translation error:", err);
      return text; // fallback to English text
    }
  };

  /**
   * Pick the best matching voice for a language code.
   * Uses exact BCP-47 prefix matching (e.g. "hi" matches "hi-IN" but not "zh").
   */
  const pickVoice = (langCode: string): SpeechSynthesisVoice | undefined => {
    const prefix = LANG_CODES[langCode] ?? langCode;
    // Prefer an exact locale match first (e.g. "hi-IN"), then any voice
    // whose lang starts with the primary subtag followed by "-" or is exact.
    return (
      voices.find((v) => v.lang === `${prefix}-IN`) ||
      voices.find((v) => v.lang.startsWith(`${prefix}-`)) ||
      voices.find((v) => v.lang === prefix)
    );
  };

  const handlePlayVoice = async () => {
    if (!scheme) return;

    const synth = window.speechSynthesis;

    if (isPlaying) {
      synth.cancel();
      setIsPlaying(false);
      return;
    }

    const text = [
      `Scheme Name: ${scheme.scheme_name}.`,
      `Description: ${scheme.description}.`,
      `Benefits: ${scheme.benefits.join(", ")}.`,
      `Eligibility: ${scheme.eligibility.join(", ")}.`,
      `Required documents: ${scheme.required_documents.join(", ")}.`,
    ].join(" ");

    /* ----------- TRANSLATION ----------- */
    const translatedText =
      selectedLanguage !== "en"
        ? await translateText(text, selectedLanguage)
        : text;

    /* ----------- VOICE SELECTION ----------- */
    const voice = pickVoice(selectedLanguage);
    const locale = LANG_LOCALES[selectedLanguage] ?? "en-IN";

    const utterance = new SpeechSynthesisUtterance(translatedText);
    utterance.lang = voice ? voice.lang : locale; // always set correct locale
    if (voice) utterance.voice = voice;
    utterance.rate = 0.95;
    utterance.pitch = 1;

    utterance.onstart = () => setIsPlaying(true);
    utterance.onend = () => setIsPlaying(false);
    utterance.onerror = () => setIsPlaying(false);

    // Cancel any ongoing speech; wait a tick before speaking to avoid
    // Chromium silently dropping the new utterance right after cancel().
    synth.cancel();
    setTimeout(() => synth.speak(utterance), 150);
  };

  /* ---------------- LOADING ---------------- */

  if (loading) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <p>Loading scheme...</p>
      </div>
    );
  }

  if (!scheme) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold mb-4">Scheme not found</h1>
          <Link to="/schemes">
            <Button>Back to Schemes</Button>
          </Link>
        </div>
      </div>
    );
  }

  const getMatchColor = (score: number) => {
    if (score >= 80) return "bg-success text-success-foreground";
    if (score >= 60) return "bg-primary text-primary-foreground";
    if (score >= 40) return "bg-secondary text-secondary-foreground";
    return "bg-muted text-muted-foreground";
  };

  return (
    <div className="min-h-screen bg-background">
      <Navbar />

      <main className="pt-24 pb-20">
        <div className="container mx-auto px-4">
          <Link
            to="/schemes"
            className="inline-flex items-center gap-2 text-muted-foreground hover:text-foreground transition-colors mb-6"
          >
            <ArrowLeft className="w-4 h-4" />
            Back to Schemes
          </Link>

          <div className="grid lg:grid-cols-3 gap-8">

            <div className="lg:col-span-2 space-y-6">

              {/* HEADER */}

              <div className="p-6 rounded-2xl bg-card border border-border">

                <div className="flex items-start justify-between gap-4 mb-4">

                  <div>

                    <div className="flex items-center gap-2 mb-2 flex-wrap">

                      <Badge variant="outline">
                        <Tag className="w-3 h-3 mr-1" />
                        {scheme.sector}
                      </Badge>

                      {scheme.category && (
                        <Badge variant="secondary">
                          {scheme.category}
                        </Badge>
                      )}

                      {scheme.matchScore && (
                        <div
                          className={cn(
                            "px-2 py-0.5 rounded-full text-xs font-semibold",
                            getMatchColor(scheme.matchScore)
                          )}
                        >
                          {scheme.matchScore}% Match
                        </div>
                      )}

                    </div>

                    <h1 className="font-display text-2xl md:text-3xl font-bold text-foreground">
                      {scheme.scheme_name}
                    </h1>

                  </div>

                  <div className="w-16 h-16 rounded-xl bg-primary/10 flex items-center justify-center shrink-0">
                    <Award className="w-8 h-8 text-primary" />
                  </div>

                </div>

                <div className="flex flex-wrap gap-4 text-sm text-muted-foreground">

                  <div className="flex items-center gap-1.5">
                    <Building2 className="w-4 h-4" />
                    <span>{scheme.ministry}</span>
                  </div>
                  

                </div>

              </div>

              {/* VOICE ASSISTANCE */}

              <div className="p-6 rounded-2xl bg-card border border-border">

                <div className="flex items-center justify-between mb-4">

                  <h2 className="font-semibold flex items-center gap-2">
                    <Volume2 className="w-5 h-5 text-primary" />
                    Voice Assistance
                  </h2>

                  <div className="flex items-center gap-2">
                    <Languages className="w-4 h-4" />

                    <select
                      value={selectedLanguage}
                      onChange={(e) => setSelectedLanguage(e.target.value)}
                      className="border rounded-lg px-2 py-1 text-sm"
                    >
                      <option value="en">English</option>
                      <option value="hi">Hindi</option>
                      <option value="ml">Malayalam</option>
                    </select>
                  </div>

                </div>

                <Button
                  onClick={handlePlayVoice}
                  className={cn(isPlaying && "animate-pulse")}
                >
                  <Volume2 className="w-4 h-4 mr-2" />
                  {isPlaying ? "Stop Voice" : "Listen to Scheme"}
                </Button>

              </div>

              {/* DESCRIPTION */}

              <div className="p-6 rounded-2xl bg-card border border-border">
                <h2 className="font-display text-lg font-semibold mb-4">
                  About This Scheme
                </h2>
                <p className="text-muted-foreground">
                  {scheme.description}
                </p>
              </div>

              {/* ELIGIBILITY */}

              <div className="p-6 rounded-2xl bg-card border border-border">

                <h2 className="font-display text-lg font-semibold mb-4">
                  Eligibility Criteria
                </h2>

                <ul className="space-y-3">
                  {scheme.eligibility.map((item, index) => (
                    <li key={index} className="flex items-start gap-3">
                      <Check className="w-4 h-4 text-green-500 mt-1" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>

              </div>

              {/* DOCUMENTS */}

              <div className="p-6 rounded-2xl bg-card border border-border">

                <h2 className="font-display text-lg font-semibold mb-4 flex items-center gap-2">
                  <FileText className="w-5 h-5 text-primary" />
                  Required Documents
                </h2>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">

                  {scheme.required_documents.map((doc, index) => (
                    <div
                      key={index}
                      className="flex items-center gap-3 p-3 rounded-xl bg-muted/50"
                    >

                      <div className="w-8 h-8 rounded-lg bg-primary/10 flex items-center justify-center">
                        <FileText className="w-4 h-4 text-primary" />
                      </div>

                      <span className="text-sm">{doc}</span>

                    </div>
                  ))}

                </div>

              </div>

            </div>

            {/* SIDEBAR */}

            <div className="space-y-6">

              <div className="p-6 rounded-2xl gradient-hero text-primary-foreground">

                <h3 className="font-display text-lg font-semibold mb-2">
                  Scheme Benefits
                </h3>

                <ul className="space-y-2 text-sm">
                  {scheme.benefits.map((b, i) => (
                    <li key={i}>• {b}</li>
                  ))}
                </ul>

              </div>

              <div className="p-6 rounded-2xl bg-card border border-border space-y-4">

                <Button
  size="lg"
  className="w-full"
  onClick={() =>
    navigate(`/demo-form/${scheme.scheme_id}`)
  }
>
  Practice Form Filling
</Button>

                <Button
                  variant="outline"
                  size="lg"
                  className="w-full gap-2"
                  onClick={() => {
                    const url =
                      "https://www.myscheme.gov.in/search?query=" +
                      encodeURIComponent(scheme.scheme_name);
                    window.open(url, "_blank", "noopener,noreferrer");
                  }}
                >
                  Apply on Official Portal
                  <ExternalLink className="w-4 h-4" />
                </Button>

              </div>

            </div>

          </div>

        </div>
      </main>

      <Footer />
      <Chatbot />
    </div>
  );
};

export default SchemeDetail;
