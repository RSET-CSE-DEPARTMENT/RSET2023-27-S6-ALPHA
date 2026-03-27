class AppConfig {
  static const String groqApiKey = String.fromEnvironment('GROQ_API_KEY');
  static const bool hasGroqApiKey = groqApiKey != '';

  // You can add other global constants here
  static const bool debugMode = true;
}
