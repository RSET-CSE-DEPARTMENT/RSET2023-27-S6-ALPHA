import { useState } from "react";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { ShieldCheck, PlusCircle, CheckCircle2, Loader2, AlertCircle } from "lucide-react";

const BACKEND = "http://localhost:8000";

// Pre-filled demo scheme — matches profile: Female, Education sector
const DEMO_SCHEME = {
  scheme_id: "DEMO_EDU_2026",
  scheme_name: "National Merit Scholarship for Higher Education 2026",
  sector: "education",
  description:
    "A new scholarship providing financial support to meritorious students for pursuing higher education in India. Open to all categories with special consideration for female students.",
  eligibility: {
    gender: "Any",
    state: "All India",
    sector: "education",
    min_age: 17,
    max_age: 30,
    education: "Graduate",
    category: "Any",
  },
  benefits: {
    scholarship_amount: "₹50,000 per year",
    duration: "Up to 3 years",
    additional: "Laptop grant of ₹15,000",
  },
  documents_required: [
    "Aadhaar Card",
    "Mark Sheets (last 2 years)",
    "Income Certificate",
    "Bank Account Details",
    "Admission Letter",
  ],
  application_process: {
    mode: "Online",
    portal: "scholarships.gov.in",
    deadline: "2026-06-30",
  },
  keywords: ["scholarship", "merit", "higher education", "financial support", "students"],
  state: "All India",
};

const Admin = () => {
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");
  const [result, setResult] = useState<{
    notifications_sent?: number;
    total_profiles?: number;
    message?: string;
  } | null>(null);

  const handleAddScheme = async () => {
    setStatus("loading");
    setResult(null);
    try {
      const res = await fetch(`${BACKEND}/admin/add-scheme`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(DEMO_SCHEME),
      });
      const data = await res.json();
      if (res.ok) {
        setStatus("success");
        setResult(data);
      } else {
        setStatus("error");
        setResult({ message: data.detail || "Something went wrong" });
      }
    } catch (err) {
      setStatus("error");
      setResult({ message: "Could not reach backend. Is it running?" });
    }
  };

  return (
    <div className="min-h-screen bg-background">
      <Navbar />

      <main className="container mx-auto px-4 py-8 pt-24 max-w-2xl">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <div className="w-10 h-10 rounded-xl bg-primary flex items-center justify-center">
            <ShieldCheck className="w-5 h-5 text-primary-foreground" />
          </div>
          <div>
            <h1 className="font-display text-2xl font-bold text-foreground">Admin Panel</h1>
            <p className="text-sm text-muted-foreground">Demo controls for presentation</p>
          </div>
          <Badge variant="secondary" className="ml-auto">Demo Mode</Badge>
        </div>

        {/* Add Scheme Card */}
        <div className="border border-border rounded-2xl bg-card p-6 shadow-sm">
          <div className="flex items-start gap-4 mb-5">
            <div className="w-9 h-9 rounded-lg bg-secondary/10 flex items-center justify-center flex-shrink-0 mt-1">
              <PlusCircle className="w-5 h-5 text-secondary" />
            </div>
            <div>
              <h2 className="font-semibold text-lg text-foreground">Add New Scheme</h2>
              <p className="text-sm text-muted-foreground mt-1">
                Adds a new scheme to the Supabase database and automatically sends
                notifications to all users whose profile matches the scheme's eligibility.
              </p>
            </div>
          </div>

          {/* Scheme Preview */}
          <div className="bg-muted/40 border border-border rounded-xl p-4 mb-5 text-sm space-y-1">
            <p className="font-medium text-foreground">{DEMO_SCHEME.scheme_name}</p>
            <p className="text-muted-foreground">{DEMO_SCHEME.description}</p>
            <div className="flex flex-wrap gap-2 mt-2">
              <Badge variant="outline" className="text-xs">{DEMO_SCHEME.sector}</Badge>
              <Badge variant="outline" className="text-xs">{DEMO_SCHEME.state}</Badge>
              <Badge variant="outline" className="text-xs">
                Age {DEMO_SCHEME.eligibility.min_age}–{DEMO_SCHEME.eligibility.max_age}
              </Badge>
            </div>
          </div>

          {/* Action Button */}
          <Button
            onClick={handleAddScheme}
            disabled={status === "loading"}
            className="w-full gap-2"
            size="lg"
          >
            {status === "loading" ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                Adding scheme & sending notifications...
              </>
            ) : (
              <>
                <PlusCircle className="w-4 h-4" />
                + Add Scheme & Notify Matched Users
              </>
            )}
          </Button>

          {/* Result */}
          {status === "success" && result && (
            <div className="mt-4 p-4 rounded-xl bg-green-500/10 border border-green-500/30 flex items-start gap-3">
              <CheckCircle2 className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
              <div>
                <p className="font-semibold text-green-700 dark:text-green-400">
                  ✅ {result.message}
                </p>
                <p className="text-sm text-muted-foreground mt-1">
                  Checked <strong>{result.total_profiles}</strong> user profiles →{" "}
                  <strong>{result.notifications_sent}</strong> notification(s) sent.
                  <br />
                  <span className="text-green-600 dark:text-green-400 font-medium">
                    Users will see the 🔔 bell light up when they refresh!
                  </span>
                </p>
              </div>
            </div>
          )}

          {status === "error" && result && (
            <div className="mt-4 p-4 rounded-xl bg-red-500/10 border border-red-500/30 flex items-start gap-3">
              <AlertCircle className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
              <p className="text-sm text-red-600 dark:text-red-400">{result.message}</p>
            </div>
          )}
        </div>

        {/* Info Note */}
        <p className="text-xs text-muted-foreground text-center mt-6">
          This page is for demo purposes. In production, this would be protected by an admin role.
        </p>
      </main>

      <Footer />
    </div>
  );
};

export default Admin;
