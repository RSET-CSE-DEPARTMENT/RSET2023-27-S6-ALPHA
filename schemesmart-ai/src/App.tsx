import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Index from "./pages/Index";
import Schemes from "./pages/Schemes";
import SchemeDetail from "./pages/SchemeDetail";
import DemoForm from "./DemoForm";
import PracticeForm from "./pages/PracticeForm";
import Profile from "./pages/Profile";
import Dashboard from "./pages/Dashboard";
import BrowseSchemes from "./pages/BrowseSchemes";
import NotFound from "./pages/NotFound";
import Signup from "./pages/Signup";

import HowItWorks from "./pages/HowItWorks";
import Login from "./pages/login";
import Admin from "./pages/Admin";

const queryClient = new QueryClient();

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />

      <BrowserRouter>

        <Routes>

          {/* Home Page */}
          <Route path="/" element={<Index />} />

          {/* AI Recommended Schemes */}
          <Route path="/schemes" element={<Schemes />} />

          {/* Browse All Schemes */}
          <Route path="/browse-schemes" element={<BrowseSchemes />} />

          {/* Scheme Details */}
          <Route path="/scheme/:id" element={<SchemeDetail />} />

          {/* Legacy Demo Form */}
          <Route path="/form/:id" element={<DemoForm />} />

          {/* ⭐ Agentic AI Practice Form */}
          <Route path="/demo-form/:id" element={<PracticeForm />} />

          {/* User Profile */}
          <Route path="/profile" element={<Profile />} />

          {/* Dashboard */}
          <Route path="/dashboard" element={<Dashboard />} />

          {/* Authentication */}
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />

          {/* Admin Demo Panel */}
          <Route path="/admin" element={<Admin />} />

          {/* Optional Page */}
          <Route path="/how-it-works" element={<HowItWorks />} />

          {/* 404 Page */}
          <Route path="*" element={<NotFound />} />

        </Routes>

      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;