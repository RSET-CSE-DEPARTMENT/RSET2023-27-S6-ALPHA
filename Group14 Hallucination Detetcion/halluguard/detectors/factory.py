"""Factory function for creating detector instances."""

from __future__ import annotations

from halluguard.detectors.base import BaseDetector

__all__ = ["make_detector"]


def make_detector(method: str, **kwargs) -> BaseDetector:
    """Create a detector of the requested type with the given parameters.

    :param method: "transformer" is the only supported method.
    :param kwargs: Passed to the concrete detector constructor.
    :return: A concrete detector instance.
    :raises ValueError: If method is not supported.
    """
    if method == "transformer":
        from halluguard.detectors.transformer import TransformerDetector

        return TransformerDetector(**kwargs)
    else:
        raise ValueError(
            f"Unknown detector method: {method}. Currently only 'transformer' is supported."
        )
