import { useState, useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import { AuthContext } from "@/context/AuthContext";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Eye, EyeOff, CheckCircle2, XCircle } from "lucide-react";

// ─── Password strength rules ──────────────────────────────────────────────────

interface Rule {
  label: string;
  test: (pw: string) => boolean;
}

const PASSWORD_RULES: Rule[] = [
  { label: "At least 8 characters",          test: (pw) => pw.length >= 8 },
  { label: "Uppercase letter (A–Z)",          test: (pw) => /[A-Z]/.test(pw) },
  { label: "Lowercase letter (a–z)",          test: (pw) => /[a-z]/.test(pw) },
  { label: "Number (0–9)",                    test: (pw) => /[0-9]/.test(pw) },
  { label: "Special character (@#$%&*!)",     test: (pw) => /[@#$%&*!]/.test(pw) },
];

function getStrengthLabel(passed: number): { label: string; color: string } {
  if (passed <= 1) return { label: "Very Weak",  color: "bg-red-500" };
  if (passed === 2) return { label: "Weak",       color: "bg-orange-400" };
  if (passed === 3) return { label: "Fair",       color: "bg-yellow-400" };
  if (passed === 4) return { label: "Strong",     color: "bg-blue-500" };
  return              { label: "Very Strong", color: "bg-green-500" };
}

// ─── Component ────────────────────────────────────────────────────────────────

const Signup = () => {
  const [email,    setEmail]    = useState("");
  const [password, setPassword] = useState("");
  const [fullName, setFullName] = useState("");
  const [showPw,   setShowPw]   = useState(false);
  const [touched,  setTouched]  = useState(false);   // only show checklist after first keystroke
  const [error,    setError]    = useState("");
  const [loading,  setLoading]  = useState(false);

  const auth     = useContext(AuthContext);
  const navigate = useNavigate();

  // Rule check results
  const ruleResults = PASSWORD_RULES.map((r) => r.test(password));
  const passedCount = ruleResults.filter(Boolean).length;
  const allPassed   = passedCount === PASSWORD_RULES.length;
  const { label: strengthLabel, color: strengthColor } = getStrengthLabel(passedCount);

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    // Client-side guard before even hitting the server
    if (!allPassed) {
      setTouched(true);
      setError("Please meet all password requirements before signing up.");
      return;
    }

    setLoading(true);
    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/signup`, {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password, full_name: fullName }),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.detail || "Signup failed. Try another email.");
      }

      if (data.access_token) {
        auth?.login(data.access_token);
      }

      navigate("/profile");
    } catch (err: unknown) {
      setError((err as Error).message || "Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-background px-4">
      <div className="w-full max-w-md p-8 border rounded-xl shadow-sm space-y-6 bg-card">

        <h1 className="text-2xl font-bold text-center">Create Your Account</h1>

        {error && (
          <p className="text-red-600 text-center text-sm bg-red-50 border border-red-200 p-3 rounded-lg">
            {error}
          </p>
        )}

        <form onSubmit={handleSignup} className="space-y-5">

          {/* Full Name */}
          <div>
            <Label htmlFor="fullName">Full Name</Label>
            <Input
              id="fullName"
              placeholder="Your full name"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              required
            />
          </div>

          {/* Email */}
          <div>
            <Label htmlFor="email">Email</Label>
            <Input
              id="email"
              type="email"
              placeholder="yourname@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          {/* Password + show/hide toggle */}
          <div className="space-y-2">
            <Label htmlFor="password">Password</Label>
            <div className="relative">
              <Input
                id="password"
                type={showPw ? "text" : "password"}
                placeholder="Create a strong password"
                value={password}
                onChange={(e) => {
                  setPassword(e.target.value);
                  setTouched(true);
                }}
                required
                className="pr-10"
              />
              <button
                type="button"
                onClick={() => setShowPw((v) => !v)}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-muted-foreground hover:text-foreground transition-colors"
                aria-label={showPw ? "Hide password" : "Show password"}
              >
                {showPw ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
              </button>
            </div>

            {/* Strength bar — shows as soon as user starts typing */}
            {touched && password.length > 0 && (
              <div className="space-y-2">
                {/* Bar */}
                <div className="flex items-center gap-2">
                  <div className="flex-1 h-1.5 bg-muted rounded-full overflow-hidden">
                    <div
                      className={`h-full rounded-full transition-all duration-300 ${strengthColor}`}
                      style={{ width: `${(passedCount / PASSWORD_RULES.length) * 100}%` }}
                    />
                  </div>
                  <span className="text-xs font-medium text-muted-foreground w-20 text-right">
                    {strengthLabel}
                  </span>
                </div>

                {/* Rule checklist */}
                <ul className="space-y-1">
                  {PASSWORD_RULES.map((rule, i) => (
                    <li key={i} className="flex items-center gap-2 text-xs">
                      {ruleResults[i] ? (
                        <CheckCircle2 className="w-3.5 h-3.5 text-green-500 shrink-0" />
                      ) : (
                        <XCircle className="w-3.5 h-3.5 text-red-400 shrink-0" />
                      )}
                      <span className={ruleResults[i] ? "text-green-700" : "text-muted-foreground"}>
                        {rule.label}
                      </span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          <Button
            type="submit"
            className="w-full"
            disabled={loading || (touched && !allPassed)}
          >
            {loading ? "Creating account..." : "Sign Up"}
          </Button>

        </form>

        <p className="text-center text-sm text-muted-foreground">
          Already have an account?{" "}
          <Link to="/login" className="text-primary hover:underline font-medium">
            Log in
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Signup;