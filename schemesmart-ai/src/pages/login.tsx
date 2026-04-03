import { useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import { useNavigate, Link } from "react-router-dom";

const Login = () => {

  const auth = useContext(AuthContext);
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async (e: React.FormEvent) => {

    e.preventDefault();

    setLoading(true);
    setError("");

    try {

      const formData = new URLSearchParams();
      formData.append("username", email);
      formData.append("password", password);

      const res = await fetch(`${import.meta.env.VITE_API_URL}/login`, {

        method: "POST",

        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },

        body: formData,

      });

      if (!res.ok) {
        setError("Invalid email or password");
        return;
      }

      const data = await res.json();

      console.log("LOGIN RESPONSE:", data);

      if (!data.access_token) {
        setError("Login failed. Token not received.");
        return;
      }

      /* SAVE TOKEN */

      auth?.login(data.access_token);

      console.log("TOKEN SAVED:", data.access_token);

      /* REDIRECT */

      navigate("/profile");

    } catch (err) {

      console.error("Login error:", err);
      setError("Server error. Please try again.");

    } finally {

      setLoading(false);

    }

  };

  return (

    <div className="min-h-screen flex items-center justify-center bg-background px-4">

      <div className="w-full max-w-md p-8 border rounded-xl shadow-sm space-y-6 bg-card">

        <h2 className="text-2xl font-bold text-center">
          Login to SchemeSmart AI
        </h2>

        {error && (
          <p className="text-red-600 text-center text-sm bg-red-50 p-3 rounded">
            {error}
          </p>
        )}

        <form onSubmit={handleLogin} className="space-y-5">

          <div>
            <label className="text-sm font-medium">Email</label>

            <input
              className="border p-2 w-full rounded mt-1"
              placeholder="your@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />

          </div>

          <div>

            <label className="text-sm font-medium">Password</label>

            <input
              type="password"
              className="border p-2 w-full rounded mt-1"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />

          </div>

          <button
            type="submit"
            disabled={loading}
            className="bg-green-600 text-white w-full py-2 rounded hover:bg-green-700 transition"
          >
            {loading ? "Logging in..." : "Login"}
          </button>

        </form>

        <div className="text-center text-sm text-muted-foreground">

          Don't have an account?{" "}

          <Link
            to="/signup"
            className="text-blue-600 hover:underline font-medium"
          >
            Sign Up
          </Link>

        </div>

      </div>

    </div>

  );

};

export default Login;