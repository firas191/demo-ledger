from datetime import date

import pytest

from ledger.models import Transaction
from ledger.reports import monthly_summary, monthly_total


def test_monthly_total_keeps_cents():
    transactions = [
        Transaction(10.50, "EUR", date(2026, 5, 3), "books"),
        Transaction(20.00, "TND", date(2026, 5, 10), "coffee"),
    ]
    # 10.50 EUR -> 11.34 USD, 20 TND -> 6.40 USD
    assert monthly_total(transactions, 5) == pytest.approx(17.74)


def test_monthly_total_filters_other_months():
    transactions = [
        Transaction(15.00, "USD", date(2026, 6, 1), "groceries"),
        Transaction(99.00, "USD", date(2026, 7, 1), "rent share"),
    ]
    assert monthly_total(transactions, 6) == pytest.approx(15.00)


def test_monthly_summary_format():
    transactions = [Transaction(15.00, "USD", date(2026, 6, 1))]
    assert monthly_summary(transactions, 6) == "1 transactions, total $15.00"
