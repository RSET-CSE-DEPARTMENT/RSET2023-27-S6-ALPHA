import { useState, useContext, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "@/context/AuthContext";
import { useUserProfile } from "@/context/UserProfileContext";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import Chatbot from "@/components/chatbot/Chatbot";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Select, SelectTrigger, SelectValue, SelectContent, SelectItem
} from "@/components/ui/select";
import { Checkbox } from "@/components/ui/checkbox";
import { ArrowRight, Sparkles, CheckCircle, Pencil, User } from "lucide-react";
import { sectors, Sector } from "@/data/schemes";

// ─── Static Data ─────────────────────────────────────────────────────────────

const educationLevels = [
  "Below Class 10", "Class 10", "Class 12", "Diploma", "Undergraduate", "Postgraduate"
];

const incomeRanges = [
  "Below ₹1 Lakh", "₹1 – ₹2.5 Lakh", "₹2.5 – ₹5 Lakh", "Above ₹5 Lakh"
];

const categories = ["General", "OBC", "SC", "ST", "Minority", "EWS"];

const indianStates = [
  "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
  "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
  "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
  "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
  "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
  "Andaman & Nicobar Islands", "Chandigarh", "Dadra & Nagar Haveli and Daman & Diu",
  "Delhi", "Jammu & Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
];

const farmingTypes = [
  "Subsistence Farming", "Organic Farming", "Commercial Farming",
  "Mixed Farming", "Horticulture", "Dairy Farming", "Poultry Farming", "Other"
];

const landholdingSizes = [
  "Landless", "Below 1 Acre", "1–2 Acres", "2–5 Acres", "5–10 Acres", "Above 10 Acres"
];

const SECTORS_WITH_EXTRA = ["Agriculture", "Women & Child Welfare", "Healthcare", "Education", "Housing"];

const sectorIcons: Record<string, string> = {
  "Education": "🎓",
  "Healthcare": "🏥",
  "Agriculture": "🌾",
  "Women & Child Welfare": "👩‍👧",
  "Housing": "🏠",
};

// ─── Empty Form ───────────────────────────────────────────────────────────────

const EMPTY_FORM = {
  name: "", age: "", gender: "",
  education: "", income: "", category: "", state: "", maritalStatus: "",
  district: "", occupation: "", disabilityStatus: "",
  selectedSectors: [] as Sector[],
  landholdingSize: "", typeOfFarming: "",
  singleGirlChild: "", pregnancyStatus: "",
  chronicIllness: "", healthInsurance: "",
  lastExamPercentage: "", scholarshipNeeded: "",
  puccaHouseStatus: "", previousSubsidy: "",
};

// ─── Summary View ─────────────────────────────────────────────────────────────

function ProfileSummary({ saved, onEdit, onFindSchemes, loadingSchemes }: {
  saved: Record<string, string>;
  onEdit: () => void;
  onFindSchemes: () => void;
  loadingSchemes: boolean;
}) {
  const fields = [
    { label: "Full Name", key: "full_name" },
    { label: "Age", key: "age" },
    { label: "Gender", key: "gender" },
    { label: "Education", key: "education" },
    { label: "Annual Income", key: "annual_income" },
    { label: "Category", key: "category" },
    { label: "State", key: "state" },
    { label: "District", key: "district" },
    { label: "Marital Status", key: "marital_status" },
    { label: "Occupation", key: "occupation" },
    { label: "Disability Status", key: "disability_status" },
    { label: "Preferred Sectors", key: "preferred_sectors" },
    { label: "Landholding Size", key: "landholding_size" },
    { label: "Type of Farming", key: "type_of_farming" },
    { label: "Single Girl Child", key: "single_girl_child" },
    { label: "Pregnancy/Lactation", key: "pregnancy_status" },
    { label: "Chronic Illness", key: "chronic_illness" },
    { label: "Health Insurance", key: "health_insurance" },
    { label: "Last Exam %", key: "last_exam_percentage" },
    { label: "Scholarship Needed", key: "scholarship_needed" },
    { label: "Pucca House", key: "pucca_house_status" },
    { label: "Previous Subsidy", key: "previous_subsidy" },
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-14 h-14 rounded-full bg-primary/10 flex items-center justify-center">
            <User className="w-7 h-7 text-primary" />
          </div>
          <div>
            <h2 className="text-xl font-bold">{saved.full_name || "Your Profile"}</h2>
            <p className="text-sm text-muted-foreground">{saved.preferred_sectors || "No sectors selected"}</p>
          </div>
        </div>
        <Button variant="outline" onClick={onEdit} className="gap-2">
          <Pencil className="w-4 h-4" /> Edit Profile
        </Button>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {fields.map(({ label, key }) =>
          saved[key] ? (
            <div key={key} className="bg-muted/50 rounded-lg p-3">
              <p className="text-xs text-muted-foreground mb-0.5">{label}</p>
              <p className="text-sm font-medium">{saved[key]}</p>
            </div>
          ) : null
        )}
      </div>

      <Button onClick={onFindSchemes} disabled={loadingSchemes} className="w-full gap-2">
        <Sparkles className="w-4 h-4" />
        {loadingSchemes ? "Finding Schemes..." : "Find Recommended Schemes"}
      </Button>
    </div>
  );
}

// ─── Main Component ───────────────────────────────────────────────────────────

export default function Profile() {
  const auth = useContext(AuthContext);
  const navigate = useNavigate();
  const { setProfile } = useUserProfile();

  // View state: "loading" | "summary" | "form"
  const [view, setView] = useState<"loading" | "summary" | "form">("loading");
  const [savedProfile, setSavedProfile] = useState<Record<string, string>>({});

  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [loadingSchemes, setLoadingSchemes] = useState(false);
  const [error, setError] = useState("");
  const topRef = useRef<HTMLDivElement>(null);

  const [formData, setFormData] = useState(EMPTY_FORM);

  const set = (key: string, val: string) => setFormData(f => ({ ...f, [key]: val }));

  const toggleSector = (sector: Sector) => {
    setFormData(prev => {
      const updated = prev.selectedSectors.includes(sector)
        ? prev.selectedSectors.filter(s => s !== sector)
        : [...prev.selectedSectors, sector];
      return { ...prev, selectedSectors: updated };
    });
  };

  // ── Load existing profile on mount ──────────────────────────────────────────

  useEffect(() => {
    const fetchProfile = async () => {
      if (!auth?.token) {
        setView("form");
        return;
      }
      try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/profile`, {
          headers: { Authorization: `Bearer ${auth.token}` },
        });
        const data = await res.json();

        // If profile has meaningful data, show summary
        if (res.ok && data && data.gender) {
          setSavedProfile(data);
          setView("summary");
          // Pre-fill form for edit mode
          setFormData({
            name: data.full_name || "",
            age: data.age || "",
            gender: data.gender || "",
            education: data.education || "",
            income: data.annual_income || "",
            category: data.category || "",
            state: data.state || "",
            maritalStatus: data.marital_status || "",
            district: data.district || "",
            occupation: data.occupation || "",
            disabilityStatus: data.disability_status || "",
            selectedSectors: (data.preferred_sectors || "").split(",").filter(Boolean) as Sector[],
            // Agriculture
            landholdingSize: data.landholding_size || "",
            typeOfFarming: data.type_of_farming || "",
            // Women & Child
            singleGirlChild: data.single_girl_child || "",
            pregnancyStatus: data.pregnancy_status || "",
            // Healthcare
            chronicIllness: data.chronic_illness || "",
            healthInsurance: data.health_insurance || "",
            // Education
            lastExamPercentage: data.last_exam_percentage || "",
            scholarshipNeeded: data.scholarship_needed || "",
            // Housing
            puccaHouseStatus: data.pucca_house_status || "",
            previousSubsidy: data.previous_subsidy || "",
          });
        } else {
          setView("form");
        }
      } catch {
        setView("form");
      }
    };

    fetchProfile();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [auth?.token]);

  // ── Derived state ────────────────────────────────────────────────────────────

  const hasSelectedSectorWithExtra = formData.selectedSectors.some(s => SECTORS_WITH_EXTRA.includes(s));
  const totalSteps = hasSelectedSectorWithExtra ? 4 : 3;

  const nextStep = () => {
    setStep(s => s + 1);
    setTimeout(() => topRef.current?.scrollIntoView({ behavior: "smooth" }), 50);
  };
  const prevStep = () => {
    setStep(s => s - 1);
    setTimeout(() => topRef.current?.scrollIntoView({ behavior: "smooth" }), 50);
  };

  // ── YesNo helper ─────────────────────────────────────────────────────────────

  const YesNo = ({ label, field }: { label: string; field: string }) => (
    <div className="space-y-1">
      <Label>{label}</Label>
      <Select value={(formData as unknown as Record<string, string>)[field]} onValueChange={v => set(field, v)}>
        <SelectTrigger><SelectValue placeholder="Select" /></SelectTrigger>
        <SelectContent>
          <SelectItem value="Yes">Yes</SelectItem>
          <SelectItem value="No">No</SelectItem>
        </SelectContent>
      </Select>
    </div>
  );

  // ── Save profile and get recommendations ─────────────────────────────────────

  const buildPayload = () => ({
    full_name: formData.name,
    age: formData.age,
    gender: formData.gender,
    education: formData.education,
    income: formData.income,
    category: formData.category,
    state: formData.state,
    marital_status: formData.maritalStatus,
    district: formData.district,
    occupation: formData.occupation,
    disability_status: formData.disabilityStatus,
    sector: formData.selectedSectors.join(","),
    landholding_size: formData.landholdingSize,
    type_of_farming: formData.typeOfFarming,
    single_girl_child: formData.singleGirlChild,
    pregnancy_status: formData.pregnancyStatus,
    chronic_illness: formData.chronicIllness,
    health_insurance: formData.healthInsurance,
    last_exam_percentage: formData.lastExamPercentage,
    scholarship_needed: formData.scholarshipNeeded,
    pucca_house_status: formData.puccaHouseStatus,
    previous_subsidy: formData.previousSubsidy,
  });

  const handleSubmit = async () => {
    try {
      setLoading(true);
      setError("");

      if (!auth?.token) {
        setError("You must be logged in. Please log in and try again.");
        return;
      }

      const profileRes = await fetch(`${import.meta.env.VITE_API_URL}/profile`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Authorization: `Bearer ${auth.token}` },
        body: JSON.stringify(buildPayload()),
      });

      if (!profileRes.ok) {
        setError("Failed to save profile.");
        return;
      }

      // After saving, go back to summary
      const updated = await fetch(`${import.meta.env.VITE_API_URL}/profile`, {
        headers: { Authorization: `Bearer ${auth.token}` },
      });
      if (updated.ok) {
        setSavedProfile(await updated.json());
      }
      setView("summary");
      setStep(1);
      await handleFindSchemes();

    } catch {
      setError("Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  const handleFindSchemes = async () => {
    try {
      setLoadingSchemes(true);

      // Merge formData + savedProfile, formData takes precedence
      const sp = savedProfile;
      const fd = formData;

      const body = {
        age:    Number(fd.age || sp.age || 0),
        gender: fd.gender || sp.gender || "",
        education:  fd.education  || sp.education  || "",
        income:     fd.income     || sp.annual_income || "",
        category:   fd.category   || sp.category   || "",
        state:      fd.state      || sp.state      || "",
        sector:     fd.selectedSectors.join(",") || sp.preferred_sectors || "",
        occupation: fd.occupation || sp.occupation || "",
        disabilityStatus: fd.disabilityStatus || sp.disability_status || "",
        // Agriculture
        landholdingSize: fd.landholdingSize || sp.landholding_size || "",
        typeOfFarming:   fd.typeOfFarming   || sp.type_of_farming  || "",
        // Women & Child
        singleGirlChild:  fd.singleGirlChild  || sp.single_girl_child  || "",
        pregnancyStatus:  fd.pregnancyStatus  || sp.pregnancy_status   || "",
        // Healthcare
        chronicIllness:  fd.chronicIllness  || sp.chronic_illness  || "",
        healthInsurance: fd.healthInsurance  || sp.health_insurance || "",
        // Education
        lastExamPercentage: fd.lastExamPercentage || sp.last_exam_percentage || "",
        scholarshipNeeded:  fd.scholarshipNeeded  || sp.scholarship_needed  || "",
        // Housing
        puccaHouseStatus: fd.puccaHouseStatus || sp.pucca_house_status || "",
        previousSubsidy:  fd.previousSubsidy  || sp.previous_subsidy  || "",
      };

      const res = await fetch(`${import.meta.env.VITE_API_URL}/recommend`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });

      if (!res.ok) return;

      const data = await res.json();
      setProfile({
        age:    String(body.age),
        gender: body.gender,
        education:  body.education,
        income:     body.income,
        category:   body.category,
        state:      body.state,
        preferred_sectors: body.sector,
        recommendations: data.recommendations || [],
      });

      navigate("/schemes");
    } finally {
      setLoadingSchemes(false);
    }
  };

  // ── Render ───────────────────────────────────────────────────────────────────

  const stepLabels = ["Basic Info", "Background", "Sectors", ...(hasSelectedSectorWithExtra ? ["Sector Details"] : [])];

  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      <main className="pt-24 pb-20">
        <div className="container mx-auto max-w-2xl px-4" ref={topRef}>

          {/* ── Loading ─────────────────────────── */}
          {view === "loading" && (
            <div className="flex items-center justify-center h-64">
              <div className="animate-spin w-8 h-8 border-4 border-primary border-t-transparent rounded-full" />
            </div>
          )}

          {/* ── Summary ─────────────────────────── */}
          {view === "summary" && (
            <>
              <h1 className="text-2xl font-bold mb-6">Your Profile</h1>
              <div className="border rounded-xl p-6 bg-card">
                <ProfileSummary
                  saved={savedProfile}
                  onEdit={() => { setView("form"); setStep(1); }}
                  onFindSchemes={handleFindSchemes}
                  loadingSchemes={loadingSchemes}
                />
              </div>
            </>
          )}

          {/* ── Form ────────────────────────────── */}
          {view === "form" && (
            <>
              {/* Progress */}
              <div className="mb-8">
                <div className="flex items-center justify-between mb-2">
                  <h1 className="text-2xl font-bold">
                    {savedProfile.gender ? "Edit Profile" : "Build Your Profile"}
                  </h1>
                  <span className="text-sm text-muted-foreground">Step {step} of {totalSteps}</span>
                </div>
                <div className="w-full bg-muted rounded-full h-2">
                  <div className="bg-primary h-2 rounded-full transition-all duration-300" style={{ width: `${(step / totalSteps) * 100}%` }} />
                </div>
                <div className="flex gap-2 mt-3">
                  {stepLabels.map((label, i) => (
                    <span key={i} className={`text-xs px-2 py-0.5 rounded-full ${i + 1 === step ? "bg-primary text-primary-foreground" : i + 1 < step ? "bg-primary/20 text-primary" : "bg-muted text-muted-foreground"}`}>
                      {i + 1 < step && <CheckCircle className="inline w-3 h-3 mr-0.5" />}{label}
                    </span>
                  ))}
                </div>
              </div>

              <div className="border rounded-xl p-6 space-y-5 bg-card">

                {/* STEP 1 */}
                {step === 1 && (
                  <>
                    <div className="space-y-1">
                      <Label>Full Name</Label>
                      <Input placeholder="Your full name" value={formData.name} onChange={e => set("name", e.target.value)} />
                    </div>
                    <div className="space-y-1">
                      <Label>Age</Label>
                      <Input type="number" placeholder="Your age" value={formData.age} onChange={e => set("age", e.target.value)} />
                    </div>
                    <div className="space-y-1">
                      <Label>Gender</Label>
                      <Select value={formData.gender} onValueChange={v => set("gender", v)}>
                        <SelectTrigger><SelectValue placeholder="Select gender" /></SelectTrigger>
                        <SelectContent>
                          <SelectItem value="Male">Male</SelectItem>
                          <SelectItem value="Female">Female</SelectItem>
                          <SelectItem value="Other">Other</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>
                  </>
                )}

                {/* STEP 2 */}
                {step === 2 && (
                  <>
                    <div className="space-y-1">
                      <Label>Education</Label>
                      <Select value={formData.education} onValueChange={v => set("education", v)}>
                        <SelectTrigger><SelectValue placeholder="Select education level" /></SelectTrigger>
                        <SelectContent>{educationLevels.map(e => <SelectItem key={e} value={e}>{e}</SelectItem>)}</SelectContent>
                      </Select>
                    </div>
                    <div className="space-y-1">
                      <Label>Annual Income</Label>
                      <Select value={formData.income} onValueChange={v => set("income", v)}>
                        <SelectTrigger><SelectValue placeholder="Select income range" /></SelectTrigger>
                        <SelectContent>{incomeRanges.map(i => <SelectItem key={i} value={i}>{i}</SelectItem>)}</SelectContent>
                      </Select>
                    </div>
                    <div className="space-y-1">
                      <Label>Category</Label>
                      <Select value={formData.category} onValueChange={v => set("category", v)}>
                        <SelectTrigger><SelectValue placeholder="Select category" /></SelectTrigger>
                        <SelectContent>{categories.map(c => <SelectItem key={c} value={c}>{c}</SelectItem>)}</SelectContent>
                      </Select>
                    </div>
                    <div className="space-y-1">
                      <Label>State</Label>
                      <Select value={formData.state} onValueChange={v => set("state", v)}>
                        <SelectTrigger><SelectValue placeholder="Select your state" /></SelectTrigger>
                        <SelectContent className="max-h-60">
                          {indianStates.map(s => <SelectItem key={s} value={s}>{s}</SelectItem>)}
                        </SelectContent>
                      </Select>
                    </div>
                    <div className="space-y-1">
                      <Label>Marital Status</Label>
                      <Select value={formData.maritalStatus} onValueChange={v => set("maritalStatus", v)}>
                        <SelectTrigger><SelectValue placeholder="Select marital status" /></SelectTrigger>
                        <SelectContent>
                          <SelectItem value="Single">Single</SelectItem>
                          <SelectItem value="Married">Married</SelectItem>
                          <SelectItem value="Widowed">Widowed</SelectItem>
                          <SelectItem value="Divorced">Divorced</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>
                    <div className="space-y-1">
                      <Label>District</Label>
                      <Input placeholder="Enter your district" value={formData.district} onChange={e => set("district", e.target.value)} />
                    </div>
                    <div className="space-y-1">
                      <Label>Occupation</Label>
                      <Input placeholder="e.g. Farmer, Student, Self-employed" value={formData.occupation} onChange={e => set("occupation", e.target.value)} />
                    </div>
                    <div className="space-y-1">
                      <Label>Disability Status</Label>
                      <Select value={formData.disabilityStatus} onValueChange={v => set("disabilityStatus", v)}>
                        <SelectTrigger><SelectValue placeholder="Select disability status" /></SelectTrigger>
                        <SelectContent>
                          <SelectItem value="None">None</SelectItem>
                          <SelectItem value="Physical">Physical</SelectItem>
                          <SelectItem value="Visual">Visual</SelectItem>
                          <SelectItem value="Hearing">Hearing</SelectItem>
                          <SelectItem value="Intellectual">Intellectual</SelectItem>
                        </SelectContent>
                      </Select>
                    </div>
                  </>
                )}

                {/* STEP 3 */}
                {step === 3 && (
                  <>
                    <p className="text-sm text-muted-foreground">Select all sectors relevant to you.</p>
                    <div className="grid grid-cols-2 gap-3">
                      {sectors.map(sector => (
                        <label key={sector} className={`flex items-center gap-3 border p-4 rounded-xl cursor-pointer transition-all ${formData.selectedSectors.includes(sector) ? "border-primary bg-primary/5" : "border-border hover:border-primary/40"}`}>
                          <Checkbox checked={formData.selectedSectors.includes(sector)} onCheckedChange={() => toggleSector(sector)} />
                          <span className="text-lg">{sectorIcons[sector]}</span>
                          <span className="text-sm font-medium">{sector}</span>
                        </label>
                      ))}
                    </div>
                  </>
                )}

                {/* STEP 4 – Sector-specific */}
                {step === 4 && hasSelectedSectorWithExtra && (
                  <div className="space-y-6">
                    <p className="text-sm text-muted-foreground">Answer a few more questions for better matching.</p>

                    {formData.selectedSectors.includes("Agriculture") && (
                      <div className="space-y-4 border rounded-lg p-4">
                        <h3 className="font-semibold text-sm">🌾 Agriculture Details</h3>
                        <div className="space-y-1">
                          <Label>Landholding Size</Label>
                          <Select value={formData.landholdingSize} onValueChange={v => set("landholdingSize", v)}>
                            <SelectTrigger><SelectValue placeholder="Select landholding size" /></SelectTrigger>
                            <SelectContent>{landholdingSizes.map(l => <SelectItem key={l} value={l}>{l}</SelectItem>)}</SelectContent>
                          </Select>
                        </div>
                        <div className="space-y-1">
                          <Label>Type of Farming</Label>
                          <Select value={formData.typeOfFarming} onValueChange={v => set("typeOfFarming", v)}>
                            <SelectTrigger><SelectValue placeholder="Select farming type" /></SelectTrigger>
                            <SelectContent>{farmingTypes.map(f => <SelectItem key={f} value={f}>{f}</SelectItem>)}</SelectContent>
                          </Select>
                        </div>
                      </div>
                    )}

                    {formData.selectedSectors.includes("Women & Child Welfare") && (
                      <div className="space-y-4 border rounded-lg p-4">
                        <h3 className="font-semibold text-sm">👩‍👧 Women & Child Details</h3>
                        <YesNo label="Single Girl Child" field="singleGirlChild" />
                        <YesNo label="Currently Pregnant or Lactating?" field="pregnancyStatus" />
                      </div>
                    )}

                    {formData.selectedSectors.includes("Healthcare") && (
                      <div className="space-y-4 border rounded-lg p-4">
                        <h3 className="font-semibold text-sm">🏥 Healthcare Details</h3>
                        <YesNo label="Chronic Illness Status" field="chronicIllness" />
                        <YesNo label="Do you have Health Insurance?" field="healthInsurance" />
                      </div>
                    )}

                    {formData.selectedSectors.includes("Education") && (
                      <div className="space-y-4 border rounded-lg p-4">
                        <h3 className="font-semibold text-sm">🎓 Education Details</h3>
                        <div className="space-y-1">
                          <Label>Minimum Percentage in Last Examination (%)</Label>
                          <Input type="number" min={0} max={100} placeholder="e.g. 75" value={formData.lastExamPercentage} onChange={e => set("lastExamPercentage", e.target.value)} />
                        </div>
                        <YesNo label="Do you need a Scholarship?" field="scholarshipNeeded" />
                      </div>
                    )}

                    {formData.selectedSectors.includes("Housing") && (
                      <div className="space-y-4 border rounded-lg p-4">
                        <h3 className="font-semibold text-sm">🏠 Housing Details</h3>
                        <YesNo label="Do you have a Pucca House?" field="puccaHouseStatus" />
                        <YesNo label="Have you received any housing subsidy before?" field="previousSubsidy" />
                      </div>
                    )}
                  </div>
                )}

                {error && <p className="text-red-500 text-sm">{error}</p>}

                <div className="flex justify-between pt-4">
                  {step > 1 ? (
                    <Button variant="outline" onClick={prevStep}>Back</Button>
                  ) : savedProfile.gender ? (
                    <Button variant="ghost" onClick={() => setView("summary")}>Cancel</Button>
                  ) : <div />}

                  {step < totalSteps ? (
                    <Button onClick={nextStep}>Continue <ArrowRight className="ml-2 w-4 h-4" /></Button>
                  ) : (
                    <Button onClick={handleSubmit} disabled={loading}>
                      <Sparkles className="mr-2 w-4 h-4" />
                      {loading ? "Saving..." : "Save & Find Schemes"}
                    </Button>
                  )}
                </div>
              </div>
            </>
          )}

        </div>
      </main>
      <Footer />
      <Chatbot />
    </div>
  );
}