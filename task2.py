import re
from decimal import Decimal
from typing import Callable


def generator_numbers(text: str):
    pattern = r'\b\d+.\d+\b'

    for match in re.finditer(pattern, text):
        yield Decimal(match.group())


def sum_profit(text: str, func: Callable):
    total_sum = sum(func(text))
    return total_sum


text_example = ("Загальний дохід працівника складається з декількох частин: "
                "1000.01 як основний дохід, доповнений додатковими "
                "надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text_example, generator_numbers)
print(f"Загальний дохід: {total_income}")
