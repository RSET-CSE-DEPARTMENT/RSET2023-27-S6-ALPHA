import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import Chatbot from "@/components/chatbot/Chatbot";
import { Search, Sparkles, Bookmark } from "lucide-react";
import { cn } from "@/lib/utils";
import { useUserProfile } from "@/context/UserProfileContext";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";

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
  match_score?: number;
  explanation?: string[];
}

const API_URL = import.meta.env.VITE_API_URL;

const Schemes = () => {

  const [schemes, setSchemes] = useState<Scheme[]>([]);
  const [loading, setLoading] = useState(true);

  const [searchQuery, setSearchQuery] = useState("");
  const [selectedSector, setSelectedSector] = useState("All");

  const [bookmarks, setBookmarks] = useState<Scheme[]>([]);

  const { profile } = useUserProfile();
  const navigate = useNavigate();

  /* ---------------- FETCH RECOMMENDATIONS ---------------- */

  useEffect(() => {

    const fetchSchemes = async () => {

      try {

        if (!profile) {
          setLoading(false);
          return;
        }

        const requestProfile = {
          age:    Number(profile.age),
          gender: profile.gender || "",
          education:  profile.education || "",
          income:     profile.income || "",
          category:   profile.category || "",
          state:      profile.state || "",
          sector:     profile.preferred_sectors || profile.sector || "",
          // Extended fields — pass through if in context
          occupation:        (profile as any).occupation        || "",
          disabilityStatus:  (profile as any).disability_status || "",
          // Agriculture
          landholdingSize:   (profile as any).landholding_size || "",
          typeOfFarming:     (profile as any).type_of_farming  || "",
          // Women & Child
          singleGirlChild:  (profile as any).single_girl_child  || "",
          pregnancyStatus:  (profile as any).pregnancy_status   || "",
          // Healthcare
          chronicIllness:  (profile as any).chronic_illness  || "",
          healthInsurance: (profile as any).health_insurance || "",
          // Education
          lastExamPercentage: (profile as any).last_exam_percentage || "",
          scholarshipNeeded:  (profile as any).scholarship_needed  || "",
          // Housing
          puccaHouseStatus: (profile as any).pucca_house_status || "",
          previousSubsidy:  (profile as any).previous_subsidy  || "",
          // Marital status
          maritalStatus: (profile as any).marital_status || "",
        };

        const res = await fetch(`${API_URL}/recommend`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(requestProfile)
        });

        if (!res.ok) {
          console.error("Recommendation API error");
          setLoading(false);
          return;
        }

        const data = await res.json();
        const recommendations = data.recommendations || [];

        const fullSchemes = await Promise.all(

          recommendations.map(async (rec: any) => {

            try {

              const r = await fetch(
                `${API_URL}/scheme/${rec.scheme_id}`
              );

              if (!r.ok) return null;

              const schemeData = await r.json();

              return {
                ...schemeData,
                match_score: rec.score,
                explanation: rec.explanation || []
              };

            } catch {
              return null;
            }

          })

        );

        setSchemes(fullSchemes.filter(Boolean));

      } catch (err) {

        console.error("Scheme fetch error:", err);

      } finally {

        setLoading(false);

      }

    };

    fetchSchemes();

  }, [profile]);

  /* ---------------- LOAD BOOKMARKS ---------------- */

  useEffect(() => {

    const saved = localStorage.getItem("bookmarkedSchemes");

    if (saved) {
      setBookmarks(JSON.parse(saved));
    }

  }, []);

  const toggleBookmark = (scheme: Scheme) => {

    const exists = bookmarks.find((s) => s.scheme_id === scheme.scheme_id);

    const updated = exists
      ? bookmarks.filter((s) => s.scheme_id !== scheme.scheme_id)
      : [...bookmarks, scheme];

    setBookmarks(updated);

    localStorage.setItem("bookmarkedSchemes", JSON.stringify(updated));

  };

  /* ---------------- UNIQUE SECTORS ---------------- */

  const sectors = [
    "All",
    ...Array.from(new Set(schemes.map((s) => s.sector).filter(Boolean)))
  ];

  /* ---------------- FILTER ---------------- */

  const filteredSchemes = schemes.filter((scheme) => {

    const name = (scheme.scheme_name || "").toLowerCase();

    const matchesSearch =
      name.includes(searchQuery.toLowerCase());

    const matchesSector =
      selectedSector === "All" ||
      (scheme.sector && scheme.sector === selectedSector);

    return matchesSearch && matchesSector;

  });

  if (loading) {
    return <p className="text-center mt-20">Finding schemes for you...</p>;
  }

  return (

    <div className="min-h-screen bg-background">

      <Navbar />

      <main className="pt-24 pb-20">

        <div className="container mx-auto px-4">

          <h1 className="text-3xl font-bold mb-2">
            Recommended Government Schemes
          </h1>

          <p className="text-muted-foreground mb-6">
            AI matched schemes based on your profile
          </p>

          {/* SEARCH + SECTOR FILTER */}

          <div className="flex flex-col md:flex-row gap-4 mb-6">

            {/* SEARCH */}

            <div className="flex items-center gap-2 border rounded-lg px-3 py-2 w-full md:w-1/3">

              <Search className="w-4 h-4 text-muted-foreground" />

              <input
                type="text"
                placeholder="Search schemes..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full outline-none bg-transparent"
              />

            </div>

            {/* SECTOR FILTER */}

            <select
              className="border rounded-lg px-3 py-2"
              value={selectedSector}
              onChange={(e) => setSelectedSector(e.target.value)}
            >
              {sectors.map((sec, i) => (
                <option key={i} value={sec}>
                  {sec === "All" ? "All Sectors" : sec}
                </option>
              ))}
            </select>

          </div>

          {/* SCHEMES GRID */}

          {filteredSchemes.length === 0 ? (

            <p className="text-center text-muted-foreground mt-10">
              No schemes matched your filters
            </p>

          ) : (

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">

              {filteredSchemes.map((scheme) => {

                const score = scheme.match_score
                  ? Math.round(scheme.match_score * 100)
                  : 0;

                return (

                  <div
                    key={scheme.scheme_id}
                    className="p-4 border rounded-2xl bg-card flex flex-col justify-between"
                  >

                    <div>

                      <div className="flex gap-2 mb-2 flex-wrap">

                        <Badge variant="outline">
                          {scheme.sector}
                        </Badge>

                      </div>

                      <h2 className="text-lg font-semibold mb-2">
                        {scheme.scheme_name}
                      </h2>

                      <p className="text-sm text-muted-foreground line-clamp-3">
                        {scheme.description}
                      </p>

                      {scheme.match_score !== undefined && (

                        <div className="mt-3">

                          <p className="text-sm font-medium text-green-700">
                            Match Score: {score}%
                          </p>

                          <div className="w-full bg-gray-200 rounded-full h-2 mt-1">

                            <div
                              className="bg-green-600 h-2 rounded-full"
                              style={{ width: `${score}%` }}
                            />

                          </div>

                          {scheme.explanation && scheme.explanation.length > 0 && (

                            <div className="mt-2">

                              <div className="flex items-center gap-2 text-xs text-amber-600">

                                <Sparkles className="w-4 h-4" />
                                AI Recommendation Insight

                              </div>

                              <ul className="text-xs text-muted-foreground ml-5 list-disc">

                                {scheme.explanation.map((e, i) => (
                                  <li key={i}>{e}</li>
                                ))}

                              </ul>

                            </div>

                          )}

                        </div>

                      )}

                    </div>

                    <div className="mt-4 flex justify-between items-center">

                      <Button
                        size="sm"
                        onClick={() => navigate(`/scheme/${scheme.scheme_id}`)}
                      >
                        View Details
                      </Button>

                      <button
                        onClick={() => toggleBookmark(scheme)}
                        className={cn(
                          "p-1 rounded-full hover:bg-gray-200",
                          bookmarks.find((s) => s.scheme_id === scheme.scheme_id)
                            ? "text-yellow-500"
                            : "text-muted-foreground"
                        )}
                      >
                        <Bookmark className="w-5 h-5" />
                      </button>

                    </div>

                  </div>

                );

              })}

            </div>

          )}

        </div>

      </main>

      <Footer />
      <Chatbot />

    </div>

  );
};

export default Schemes;