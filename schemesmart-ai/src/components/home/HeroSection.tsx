import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ArrowRight, Sparkles, Shield, Volume2 } from "lucide-react";
import { useContext } from "react";
import { AuthContext } from "@/context/AuthContext";

const HeroSection = () => {

  const auth = useContext(AuthContext);

  const features = [
    { icon: Shield, text: "100% Secure & Official" },
    { icon: Volume2, text: "Voice Guidance" },
    { icon: Sparkles, text: "AI-Powered Matching" },
  ];

  const stats = [
    { value: "500+", label: "Government Schemes" },
    { value: "6", label: "Sectors Covered" },
    { value: "3", label: "Languages Supported" },
    { value: "24/7", label: "AI Assistance" },
  ];

  return (
    <section className="relative min-h-screen gradient-hero overflow-hidden">

      {/* Background Decorations */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-20 left-10 w-72 h-72 bg-secondary/20 rounded-full blur-3xl animate-float" />
        <div
          className="absolute bottom-20 right-10 w-96 h-96 bg-primary-foreground/5 rounded-full blur-3xl animate-float"
          style={{ animationDelay: "2s" }}
        />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-primary-foreground/3 rounded-full blur-3xl" />
      </div>

      <div className="container mx-auto px-4 pt-32 pb-20 relative z-10">
        <div className="max-w-4xl mx-auto text-center">

          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary-foreground/10 backdrop-blur-sm border border-primary-foreground/20 mb-8 animate-fade-in">
            <Sparkles className="w-4 h-4 text-secondary" />
            <span className="text-primary-foreground/90 text-sm font-medium">
              AI-Powered Government Scheme Discovery
            </span>
          </div>

          {/* Heading */}
          <h1 className="font-display text-4xl md:text-6xl lg:text-7xl font-bold text-primary-foreground leading-tight mb-6 animate-slide-up">
            Find the{" "}
            <span className="text-gradient-accent">
              Right Government Scheme
            </span>{" "}
            for You
          </h1>

          {/* Description */}
          <p
            className="text-lg md:text-xl text-primary-foreground/80 max-w-2xl mx-auto mb-10 leading-relaxed animate-slide-up"
            style={{ animationDelay: "0.1s" }}
          >
            SchemeSmart AI helps you discover, understand, and apply for
            government schemes across Education, Healthcare, Agriculture,
            and more — with voice guidance in Malayalam & Hindi.
          </p>

          {/* CTA Buttons */}
          <div
            className="flex flex-col sm:flex-row gap-4 justify-center mb-16 animate-slide-up"
            style={{ animationDelay: "0.2s" }}
          >

            {/* Smart redirect based on login */}
            <Link to={auth?.token ? "/profile" : "/signup"}>
              <Button variant="hero" size="xl" className="gap-2">
                Get Started
                <ArrowRight className="w-5 h-5" />
              </Button>
            </Link>

            {/* Browse Schemes */}
            <Link to="/browse-schemes">
              <Button variant="heroOutline" size="xl">
                Browse Schemes
              </Button>
            </Link>

          </div>

          {/* Feature Pills */}
          <div
            className="flex flex-wrap justify-center gap-4 animate-fade-in"
            style={{ animationDelay: "0.3s" }}
          >
            {features.map((feature, index) => {
              const Icon = feature.icon;

              return (
                <div
                  key={index}
                  className="flex items-center gap-2 px-4 py-2 rounded-full bg-primary-foreground/10 backdrop-blur-sm"
                >
                  <Icon className="w-4 h-4 text-secondary" />
                  <span className="text-primary-foreground/90 text-sm font-medium">
                    {feature.text}
                  </span>
                </div>
              );
            })}
          </div>

        </div>

        {/* Stats */}
        <div
          className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto mt-20 animate-slide-up"
          style={{ animationDelay: "0.4s" }}
        >
          {stats.map((stat, index) => (
            <div
              key={index}
              className="text-center p-4 rounded-2xl bg-primary-foreground/5 backdrop-blur-sm border border-primary-foreground/10"
            >
              <div className="font-display text-3xl md:text-4xl font-bold text-secondary mb-1">
                {stat.value}
              </div>
              <div className="text-primary-foreground/70 text-sm">
                {stat.label}
              </div>
            </div>
          ))}
        </div>

      </div>

      {/* Wave Divider */}
      <div className="absolute bottom-0 left-0 right-0">
        <svg
          viewBox="0 0 1440 120"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="w-full"
        >
          <path
            d="M0 120L60 105C120 90 240 60 360 45C480 30 600 30 720 37.5C840 45 960 60 1080 67.5C1200 75 1320 75 1380 75L1440 75V120H1380C1320 120 1200 120 1080 120C960 120 840 120 720 120C600 120 480 120 360 120C240 120 120 120 60 120H0Z"
            fill="hsl(var(--background))"
          />
        </svg>
      </div>

    </section>
  );
};

export default HeroSection;