import re
from typing import Callable

def generator_numbers(text: str):
    """Генератор, що ітерує по всіх дійсних числах у тексті."""
    # Використовуємо регулярний вираз для знаходження дійсних чисел
    numbers = re.findall(r'\b\d+\.\d+\b', text)
    for number in numbers:
        yield float(number)  # Повертаємо дійсні числа як float

def sum_profit(text: str, func: Callable) -> float:
    """Обчислює загальний прибуток, використовуючи генератор."""
    total = sum(func(text))  # Викликаємо генератор і підсумовуємо числа
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")  # Виведе: Загальний дохід: 1351.46