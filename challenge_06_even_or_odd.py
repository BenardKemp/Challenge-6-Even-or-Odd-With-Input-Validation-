"""
Challenge #6: Even or Odd (With Input Validation)

Write a function that returns "Even" for even integers and "Odd" for odd integers.

Rules:
- Accept only integers.
- Treat booleans as invalid input.
- Raise TypeError for invalid input.
"""

from __future__ import annotations


def even_or_odd(n: int) -> str:
    """
    Return "Even" if n is even, "Odd" if n is odd.

    Raises:
        TypeError: if n is not an int or if n is a bool
    """
    # Input validation
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer (bool is not allowed)")

    return "Even" if n % 2 == 0 else "Odd"


