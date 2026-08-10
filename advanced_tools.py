"""Additional standalone features for the text processor calculator project."""

from typing import Iterable


def power(base: float, exponent: float) -> float:
    """Return the value of base raised to the given exponent."""
    return base ** exponent


def word_count(text: str) -> int:
    """Count the words in a string, ignoring extra whitespace."""
    cleaned = " ".join(text.split())
    return len(cleaned.split()) if cleaned else 0


def is_palindrome(text: str) -> bool:
    """Check whether the text is a palindrome, ignoring spaces and punctuation."""
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


def average(values: Iterable[float]) -> float:
    """Return the arithmetic mean of a collection of numbers."""
    numbers = list(values)
    if not numbers:
        raise ValueError("average() requires at least one number.")
    return sum(numbers) / len(numbers)
