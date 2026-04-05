import { User, Brain, Sparkles, FileText } from "lucide-react";

const steps = [
  {
    icon: User,
    title: "Create Your Profile",
    description:
      "Enter your age, education, income, category, and state to build your eligibility profile.",
  },
  {
    icon: Brain,
    title: "AI Analyzes Eligibility",
    description:
      "Our AI engine compares your profile with hundreds of government schemes using TF-IDF based recommendation algorithms.",
  },
  {
    icon: Sparkles,
    title: "Smart Recommendations",
    description:
      "The system ranks schemes based on relevance and eligibility and shows match scores with AI insights.",
  },
  {
    icon: FileText,
    title: "Apply Easily",
    description:
      "View scheme details, understand benefits, and apply with guided assistance.",
  },
];

const HowItWorksSection = () => {
  return (
    <section id="how-it-works" className="py-24 bg-background">
      <div className="container mx-auto px-4">

        {/* Title */}
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            How SchemeSmart AI Works
          </h2>

          <p className="text-muted-foreground max-w-2xl mx-auto">
            Discover government schemes that match your eligibility using our
            AI-powered recommendation system.
          </p>
        </div>

        {/* Steps */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">

          {steps.map((step, index) => {
            const Icon = step.icon;

            return (
              <div
                key={index}
                className="p-6 bg-card border border-border rounded-2xl text-center shadow-sm hover:shadow-lg transition-all duration-300"
              >
                {/* Icon */}
                <div className="flex justify-center mb-4">
                  <div className="w-12 h-12 flex items-center justify-center rounded-full bg-primary/10">
                    <Icon className="w-6 h-6 text-primary" />
                  </div>
                </div>

                {/* Title */}
                <h3 className="font-semibold text-lg mb-2">
                  {step.title}
                </h3>

                {/* Description */}
                <p className="text-sm text-muted-foreground leading-relaxed">
                  {step.description}
                </p>
              </div>
            );
          })}

        </div>

      </div>
    </section>
  );
};

export default HowItWorksSection;