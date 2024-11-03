def caching_fibonacci():
    # Створюємо порожній словник для кешу
    cache = {}

    def fibonacci(n):
        # Якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1
        elif n == 1:
            return 1
        # Перевіряємо, чи є значення в кеші
        if n in cache:
            return cache[n]

        # Обчислюємо значення рекурсивно та зберігаємо в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610