import re
from typing import Callable, Generator

def generator_numbers(text: str):
    numbers_extracted = re.findall(r'(?<=\s)-?\d+\.?\d*(?=\s)', text)
    for number in numbers_extracted:
        yield float(number)

def sum_profit(text: str, func: Callable[[str],Generator[float,None,None]])->float:
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід з простих чисел: {total_income}")
