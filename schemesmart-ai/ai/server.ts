import express from "express";
import cors from "cors";
import { schemeForms } from "../src/ai/agentic/form_schemas";

const app = express();

app.use(cors());
app.use(express.json());

/*
Get form schema
*/
app.get("/api/form/:schemeId", (req, res) => {
  const { schemeId } = req.params;

  const form = schemeForms.find((f) => f.schemeId === schemeId);

  if (!form) {
    return res.status(404).json({
      error: "Scheme form not found",
    });
  }

  res.json(form);
});

/*
Validate a field
*/
app.post("/api/validate", (req, res) => {
  const { field, value } = req.body;

  try {
    if (field.validate) {
      field.validate(value);
    }

    res.json({ success: true });
  } catch (err: any) {
    res.json({
      success: false,
      message: err.message,
    });
  }
});

app.listen(5000, () => {
  console.log("Agentic AI server running on port 5000");
});