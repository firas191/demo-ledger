"""Currency conversion helpers."""

RATES = {
    "USD": 1.0,
    "EUR": 1.08,
    "TND": 0.32,
    "GBP": 1.27,
}


def to_usd(amount: float, currency: str) -> float:
    """Convert an amount to USD using the static rate table."""
    if currency not in RATES:
        raise ValueError(f"Unknown currency: {currency}")
    rate = RATES[currency]
    return amount * rate


def supported_currencies() -> list[str]:
    return sorted(RATES)
