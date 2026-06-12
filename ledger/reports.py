"""Reporting: monthly summaries over a list of transactions."""

from .currency import to_usd
from .models import Transaction


def monthly_total(transactions: list[Transaction], month: int) -> float:
    """Total spend for a given month, in USD."""
    return sum(
        to_usd(t.amount, t.currency)
        for t in transactions
        if t.when.month == month
    )


def monthly_summary(transactions: list[Transaction], month: int) -> str:
    total = monthly_total(transactions, month)
    count = sum(1 for t in transactions if t.when.month == month)
    return f"{count} transactions, total ${total:.2f}"


def category_totals(transactions: list[Transaction], month: int) -> dict:
    """Spend per category for a given month, in USD."""
    totals: dict = {}
    for t in transactions:
        if t.when.month == month:
            key = t.description
            totals[key] = totals.get(key, 0) + to_usd(t.amount, t.currency)
    return totals
