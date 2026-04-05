import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { UserProfileProvider } from "./context/UserProfileContext";

import { AuthProvider } from "./context/AuthContext";

createRoot(document.getElementById("root")!).render(
  <AuthProvider>
    <UserProfileProvider>
      <App />
    </UserProfileProvider>
  </AuthProvider>
);



