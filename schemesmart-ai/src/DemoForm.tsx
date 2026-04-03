import React, { useState, useEffect } from "react";
import { startForm, answerQuestion } from "./lib/agentApi";
import { useParams, Link } from "react-router-dom";
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import Chatbot from "@/components/chatbot/Chatbot";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import {
  ArrowLeft,
  Check,
  AlertCircle,
  Languages,
  ArrowRight,
} from "lucide-react";

const DemoForm = () => {

  /* ---------------- GET ROUTE PARAM ---------------- */

  const { id } = useParams<{ id: string }>();
  console.log("Scheme ID:", id);

  const [scheme, setScheme] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  const [formData, setFormData] = useState<Record<string, any>>({});
  const [currentQuestion, setCurrentQuestion] = useState<any>(null);
  const [submitted, setSubmitted] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState("English");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  /* ---------------- FETCH SCHEME ---------------- */

  useEffect(() => {

    async function fetchScheme() {

      if (!id) return;

      try {

        const res = await fetch(`${import.meta.env.VITE_API_URL}/scheme/${id}`);

        if (!res.ok) {
          throw new Error("Scheme not found");
        }

        const data = await res.json();

        const schemeData = data.scheme ? data.scheme : data;

        setScheme(schemeData);

      } catch (err) {

        console.error("Failed to load scheme", err);
        setScheme(null);

      } finally {

        setLoading(false);

      }

    }

    fetchScheme();

  }, [id]);

  /* ---------------- START FORM ---------------- */

  useEffect(() => {

    async function initializeForm() {

      if (!id) return;

      try {

        console.log("Starting form for scheme:", id);

        const res = await startForm(id);

        console.log("FORM RESPONSE:", res);

        if (!res || !res.question) {
          throw new Error("No question returned from backend");
        }

        setCurrentQuestion(res.question);

      } catch (err) {

        console.error("Failed to start form", err);
        setErrorMessage("Could not start the form.");

      }

    }

    initializeForm();

  }, [id]);

  /* ---------------- LOADING ---------------- */

  if (loading) {

    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <p>Loading form...</p>
      </div>
    );

  }

  /* ---------------- SCHEME NOT FOUND ---------------- */

  if (!scheme) {

    return (
      <div className="min-h-screen bg-background flex items-center justify-center">

        <div className="text-center">

          <h1 className="text-2xl font-bold mb-4">
            Scheme not found
          </h1>

          <Link to="/schemes">
            <Button>Back to Schemes</Button>
          </Link>

        </div>

      </div>
    );

  }

  /* ---------------- NEXT QUESTION ---------------- */

  // DemoForm.tsx
async function handleNext() {
  if (!currentQuestion) return;

  const answer = formData[currentQuestion.id];
  if (!answer) {
    setErrorMessage("Please enter a value before continuing.");
    return;
  }

  try {
    const res = await answerQuestion(id, currentQuestion.id, answer);

    if (res?.error) {
      setErrorMessage(res.message);

      if (res.speak) {
        const msg = new SpeechSynthesisUtterance(res.speak);
        window.speechSynthesis.speak(msg);
      }

      return;
    }

    setErrorMessage(null);

    if (res?.completed) {
      setSubmitted(true);
      return;
    }

    setCurrentQuestion(res.question);
  } catch (err) {
    console.error("Answer submission failed", err);
    setErrorMessage("Failed to submit answer.");
  }
}
  /* ---------------- FORM COMPLETED ---------------- */

  if (submitted) {

    return (

      <div className="min-h-screen bg-background">

        <Navbar />

        <main className="pt-24 pb-20">

          <div className="container mx-auto px-4 max-w-2xl">

            <div className="text-center p-8 rounded-2xl bg-card border border-border">

              <div className="w-20 h-20 rounded-full bg-success/20 flex items-center justify-center mx-auto mb-6">
                <Check className="w-10 h-10 text-success" />
              </div>

              <h1 className="font-display text-2xl font-bold text-foreground mb-4">
                Demo Form Completed! 🎉
              </h1>

              <p className="text-muted-foreground mb-6">
                Great job! You've practiced filling the form.
              </p>

              <Link to={`/scheme/${scheme.scheme_id}`}>
                <Button variant="outline" size="lg">
                  Back to Scheme Details
                </Button>
              </Link>

            </div>

          </div>

        </main>

        <Footer />
        <Chatbot />

      </div>

    );

  }

  /* ---------------- MAIN FORM UI ---------------- */

  return (

    <div className="min-h-screen bg-background">

      <Navbar />

      <main className="pt-24 pb-20">

        <div className="container mx-auto px-4 max-w-3xl">

          <Link
            to={`/scheme/${scheme.scheme_id}`}
            className="inline-flex items-center gap-2 text-muted-foreground hover:text-foreground transition-colors mb-6"
          >
            <ArrowLeft className="w-4 h-4" />
            Back to Scheme Details
          </Link>

          <div className="p-6 rounded-2xl gradient-subtle border border-border mb-8">

            <div className="flex items-start justify-between gap-4">

              <div>

                <span className="inline-block px-3 py-1 rounded-full bg-secondary/20 text-secondary text-xs font-medium mb-2">
                  Demo Practice Form
                </span>

                <h1 className="font-display text-2xl font-bold text-foreground mb-2">
                  {scheme.scheme_name}
                </h1>

                <p className="text-muted-foreground text-sm">
                  Practice filling this form with AI guidance.
                </p>

              </div>

              <div className="flex items-center gap-2 shrink-0">

                <Languages className="w-4 h-4 text-muted-foreground" />

                <select
                  value={selectedLanguage}
                  onChange={(e) => setSelectedLanguage(e.target.value)}
                  className="text-sm bg-card border border-border rounded-lg px-3 py-1.5"
                >
                  <option>English</option>
                  <option>Malayalam</option>
                  <option>Hindi</option>
                </select>

              </div>

            </div>

          </div>

          <div className="p-6 rounded-2xl bg-card border border-border">

            {currentQuestion && (

              <div className="space-y-4">

                <Label>
                  {currentQuestion.text || currentQuestion.id.replace(/_/g, " ").toUpperCase()}
                </Label>

                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => {
                    const msg = new SpeechSynthesisUtterance(
                      currentQuestion.text || currentQuestion.id
                    );
                    window.speechSynthesis.speak(msg);
                  }}
                >
                  🔊 Listen
                </Button>

                <Input
                  value={formData[currentQuestion.id] || ""}
                  onChange={(e) =>
                    setFormData({
                      ...formData,
                      [currentQuestion.id]: e.target.value,
                    })
                  }
                />

              </div>

            )}

            {errorMessage && (
              <p className="text-red-500 mt-3">{errorMessage}</p>
            )}

            <div className="flex justify-end mt-8">

              <Button onClick={handleNext}>
                Next
                <ArrowRight className="w-4 h-4 ml-2" />
              </Button>

            </div>

          </div>

          <div className="mt-6 p-4 rounded-xl bg-accent/50 border border-border flex items-start gap-3">

            <AlertCircle className="w-5 h-5 text-primary shrink-0 mt-0.5" />

            <div>

              <p className="text-sm font-medium text-foreground">
                This is a practice form only
              </p>

              <p className="text-xs text-muted-foreground">
                Your information is not saved anywhere.
              </p>

            </div>

          </div>

        </div>

      </main>

      <Footer />
      <Chatbot />

    </div>

  );

};

export default DemoForm;