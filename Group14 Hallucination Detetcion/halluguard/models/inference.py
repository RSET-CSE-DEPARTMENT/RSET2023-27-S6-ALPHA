# halluguard/models/inference.py
"""Public façade for HalluGuard.

Down-stream code should keep importing **HallucinationDetector** from here;
the concrete detector classes now live in :pymod:`halluguard.detectors.*`.
Nothing in the public API has changed.
"""

from halluguard.detectors.factory import make_detector


class HallucinationDetector:
    """Facade class that delegates to a concrete detector chosen by *method*.

    :param method: ``"transformer"`` (token-classifier).
    :param kwargs: Passed straight through to the chosen detector's constructor.
    """

    def __init__(self, method: str = "transformer", **kwargs):
        self.detector = make_detector(method, **kwargs)

    def predict(
        self,
        context: list[str],
        answer: str,
        question: str | None = None,
        output_format: str = "tokens",
    ) -> list:
        """Predict hallucination tokens or spans given passages and an answer."""
        return self.detector.predict(context, answer, question, output_format)

    def predict_prompt(self, prompt: str, answer: str, output_format: str = "tokens") -> list:
        """Predict hallucinations when you already have a *single* full prompt string."""
        return self.detector.predict_prompt(prompt, answer, output_format)

    def predict_prompt_batch(
        self, prompts: list[str], answers: list[str], output_format: str = "tokens"
    ) -> list:
        """Batch version of :py:meth:`predict_prompt`."""
        return self.detector.predict_prompt_batch(prompts, answers, output_format)
