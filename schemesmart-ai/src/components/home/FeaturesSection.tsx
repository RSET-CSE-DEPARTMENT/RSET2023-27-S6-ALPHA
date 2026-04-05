import { Volume2, Languages, Bot, Shield, Sparkles, FileCheck } from "lucide-react";

const features = [
  {
    icon: Sparkles,
    title: "AI-Powered Matching",
    description: "Smart algorithms rank schemes based on your eligibility and success probability.",
  },
  {
    icon: Volume2,
    title: "Voice Assistance",
    description: "Listen to scheme details and form instructions in Malayalam, Hindi, and English.",
  },
  {
    icon: Languages,
    title: "Multilingual Support",
    description: "Full content and guidance available in your preferred regional language.",
  },
  {
    icon: Bot,
    title: "24/7 AI Chatbot",
    description: "Get instant answers about eligibility, documents, and application process.",
  },
  {
    icon: FileCheck,
    title: "Demo Form Practice",
    description: "Practice filling official forms with step-by-step voice guidance before applying.",
  },
  {
    icon: Shield,
    title: "Secure & Official",
    description: "We redirect you to official portals. No data is stored or submitted by us.",
  },
];

const FeaturesSection = () => {
  return (
    <section className="py-20 gradient-subtle">
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="inline-block px-4 py-1.5 rounded-full bg-primary/10 text-primary text-sm font-medium mb-4">
            Features
          </span>
          <h2 className="font-display text-3xl md:text-4xl font-bold text-foreground mb-4">
            Why Choose{" "}
            <span className="text-gradient">SchemeSmart AI</span>
          </h2>
          <p className="text-muted-foreground text-lg">
            Like having your personal Akshaya Centre, available 24/7 on your phone
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <div
              key={index}
              className="group p-6 rounded-2xl bg-card border border-border hover:border-primary/30 hover:shadow-xl transition-all duration-300"
            >
              <div className="w-12 h-12 rounded-xl bg-primary/10 flex items-center justify-center mb-4 group-hover:bg-primary group-hover:scale-110 transition-all">
                <feature.icon className="w-6 h-6 text-primary group-hover:text-primary-foreground transition-colors" />
              </div>
              <h3 className="font-display text-lg font-semibold text-foreground mb-2">
                {feature.title}
              </h3>
              <p className="text-muted-foreground text-sm leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeaturesSection;
