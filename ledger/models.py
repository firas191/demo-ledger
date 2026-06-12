from dataclasses import dataclass
from datetime import date


@dataclass
class Transaction:
    amount: float
    currency: str
    when: date
    description: str = ""
    category: str = ""
