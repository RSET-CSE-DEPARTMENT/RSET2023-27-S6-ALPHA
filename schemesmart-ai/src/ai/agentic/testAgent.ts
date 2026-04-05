const API = import.meta.env.VITE_API_URL;

/* START FORM */
export async function startForm(schemeId: string) {

  const res = await fetch(`${API}/form/start/${schemeId}`);

  if (!res.ok) {
    throw new Error("Failed to start form");
  }

  return await res.json();
}


/* ANSWER QUESTION */
export async function answerQuestion(questionId: string, answer: string) {

  const res = await fetch(`${API}/form/answer`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question_id: questionId,
      answer: answer
    }),
  });

  if (!res.ok) {
    throw new Error("Failed to submit answer");
  }

  return await res.json();
}