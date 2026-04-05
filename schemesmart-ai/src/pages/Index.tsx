import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";
import HeroSection from "@/components/home/HeroSection";
import HowItWorksSection from "@/components/home/HowItWorksSection";
import FeaturesSection from "@/components/home/FeaturesSection";
import CTASection from "@/components/home/CTASection";
import Chatbot from "@/components/chatbot/Chatbot";

const Index = () => {
  return (
    <div className="min-h-screen flex flex-col bg-background">
      
      {/* Navbar */}
      <Navbar />

      {/* Page Content */}
      <main className="flex-1">

        {/* Hero */}
        <HeroSection />

        {/* How It Works */}
        <HowItWorksSection />

        {/* Features */}
        <FeaturesSection />

        {/* Call To Action */}
        <CTASection />

      </main>

      {/* Footer */}
      <Footer />

      {/* Chatbot */}
      <Chatbot />

    </div>
  );
};

export default Index;