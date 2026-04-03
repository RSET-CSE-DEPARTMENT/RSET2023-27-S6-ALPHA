import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ArrowRight, Landmark } from "lucide-react";

const CTASection = () => {
  return (
    <section className="py-20 bg-background">
      <div className="container mx-auto px-4">
        <div className="relative rounded-3xl gradient-hero p-8 md:p-16 overflow-hidden">
          {/* Background Decorations */}
          <div className="absolute top-0 right-0 w-96 h-96 bg-secondary/20 rounded-full blur-3xl" />
          <div className="absolute bottom-0 left-0 w-72 h-72 bg-primary-foreground/5 rounded-full blur-3xl" />

          <div className="relative z-10 max-w-3xl mx-auto text-center">
            <div className="w-16 h-16 rounded-2xl bg-primary-foreground/10 flex items-center justify-center mx-auto mb-6">
              <Landmark className="w-8 h-8 text-primary-foreground" />
            </div>

            <h2 className="font-display text-3xl md:text-4xl lg:text-5xl font-bold text-primary-foreground mb-6">
              Government Benefits{" "}
              <span className="text-gradient-accent">You Deserve</span>
            </h2>

            <p className="text-lg text-primary-foreground/80 mb-8 max-w-2xl mx-auto">
              Thousands of government schemes across Education, Healthcare, Agriculture, 
              Employment, and more are waiting for you. Let AI help you find the ones 
              you're most eligible for — completely free.
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/profile">
                <Button variant="hero" size="xl" className="gap-2">
                  Start Your Journey
                  <ArrowRight className="w-5 h-5" />
                </Button>
              </Link>
              <Link to="/schemes">
                <Button variant="heroOutline" size="xl">
                  Explore Schemes
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CTASection;
