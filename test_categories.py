from datetime import date

import pytest

from ledger.models import Transaction
from ledger.reports import category_totals


def test_category_totals_groups_by_category():
    transactions = [
        Transaction(10.00, "USD", date(2026, 5, 1), "lunch at cafe", category="food"),
        Transaction(5.00, "USD", date(2026, 5, 2), "bus ticket", category="transport"),
        Transaction(20.00, "USD", date(2026, 5, 3), "dinner downtown", category="food"),
    ]
    assert category_totals(transactions, 5) == {
        "food": pytest.approx(30.00),
        "transport": pytest.approx(5.00),
    }


def test_category_totals_empty_month():
    transactions = [
        Transaction(10.00, "USD", date(2026, 5, 1), "lunch", category="food"),
    ]
    assert category_totals(transactions, 12) == {}
