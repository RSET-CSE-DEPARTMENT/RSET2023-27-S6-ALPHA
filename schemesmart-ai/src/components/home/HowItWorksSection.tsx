import { UserPlus, Filter, FileText, FormInput, ExternalLink, MessageCircle, Bell } from "lucide-react";

const steps = [
  {
    icon: UserPlus,
    title: "Create Your Profile",
    description: "Sign in and enter your details — education, income, location, category, and preferences.",
    color: "bg-primary",
  },
  {
    icon: Filter,
    title: "Get Matched Schemes",
    description: "AI filters out ineligible schemes and ranks the best ones based on your highest chances.",
    color: "bg-secondary",
  },
  {
    icon: FileText,
    title: "Understand Each Scheme",
    description: "View scheme details in simple language with voice assistance in Malayalam & Hindi.",
    color: "bg-success",
  },
  {
    icon: FormInput,
    title: "Practice Form Filling",
    description: "Use the demo form with voice guidance to learn how to fill official applications correctly.",
    color: "bg-primary",
  },
  {
    icon: ExternalLink,
    title: "Apply on Official Portal",
    description: "Get redirected to the official government website to submit your application securely.",
    color: "bg-secondary",
  },
  {
    icon: MessageCircle,
    title: "Get Help Anytime",
    description: "Use our AI chatbot for instant answers about eligibility, documents, and deadlines.",
    color: "bg-success",
  },
];

const HowItWorksSection = () => {
  return (
    <section id="how-it-works" className="py-20 bg-background">
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="text-center max-w-2xl mx-auto mb-16">
          <span className="inline-block px-4 py-1.5 rounded-full bg-accent text-accent-foreground text-sm font-medium mb-4">
            How It Works
          </span>
          <h2 className="font-display text-3xl md:text-4xl font-bold text-foreground mb-4">
            Your Journey to the{" "}
            <span className="text-gradient">Right Scheme</span>
          </h2>
          <p className="text-muted-foreground text-lg">
            Simple steps to discover and apply for government schemes with confidence
          </p>
        </div>

        {/* Steps Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {steps.map((step, index) => (
            <div
              key={index}
              className="group relative p-6 rounded-2xl bg-card border border-border hover:border-primary/30 hover:shadow-lg transition-all duration-300"
            >
              {/* Step Number */}
              <div className="absolute -top-3 -left-3 w-8 h-8 rounded-full bg-muted flex items-center justify-center border border-border text-sm font-bold text-muted-foreground">
                {index + 1}
              </div>

              {/* Icon */}
              <div className={`w-14 h-14 rounded-xl ${step.color} flex items-center justify-center mb-4 group-hover:scale-110 transition-transform`}>
                <step.icon className="w-7 h-7 text-primary-foreground" />
              </div>

              {/* Content */}
              <h3 className="font-display text-xl font-semibold text-foreground mb-2">
                {step.title}
              </h3>
              <p className="text-muted-foreground text-sm leading-relaxed">
                {step.description}
              </p>
            </div>
          ))}
        </div>

        {/* Notification Banner */}
        <div className="mt-12 p-6 rounded-2xl gradient-subtle border border-border flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <div className="w-12 h-12 rounded-xl bg-secondary flex items-center justify-center">
              <Bell className="w-6 h-6 text-secondary-foreground" />
            </div>
            <div>
              <h4 className="font-display font-semibold text-foreground">
                Never Miss a Deadline
              </h4>
              <p className="text-muted-foreground text-sm">
                Get alerts for new schemes, application deadlines, and status updates
              </p>
            </div>
          </div>
          <button className="px-6 py-2.5 rounded-lg bg-primary text-primary-foreground font-medium hover:bg-primary/90 transition-colors">
            Enable Notifications
          </button>
        </div>
      </div>
    </section>
  );
};

export default HowItWorksSection;
