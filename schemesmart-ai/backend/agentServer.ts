import express from "express";
import cors from "cors";

import { FormEngine } from "../src/ai/agentic/agentEngine.ts";
import { SCHEMES } from "../src/ai/agentic/form_schemas/index.ts";

const app = express();
app.use(cors());
app.use(express.json());

let engine: FormEngine | null = null;

app.post("/start", (req, res) => {
  const { schemeId } = req.body;

  if (!SCHEMES[schemeId]) {
    return res.status(400).json({ error: "Invalid scheme" });
  }

  engine = new FormEngine(SCHEMES[schemeId]);

  const next = engine.getNextQuestion();

  res.json({
    question: next
  });
});

app.post("/answer", (req, res) => {
  const { id, answer } = req.body;

  if (!engine) {
    return res.status(400).json({ error: "Form not started" });
  }

  const error = engine.validate(id, answer);

  if (error) {
    return res.json({
      error
    });
  }

  engine.answer(id, answer);

  const next = engine.getNextQuestion();

  if (!next) {
    return res.json({
      completed: true,
      responses: engine.getResponses()
    });
  }

  res.json({
    question: next
  });
});

app.listen(5000, () => {
  console.log("Agent server running on port 5000");
});