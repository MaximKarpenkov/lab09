def factorial(number):
    """Рекурсивно вычисляет факториал (0 <= number <= 20)."""
    if number == 0:
        return 1
    return number * factorial(number - 1)


def factorial_iterative(number):
    """Итеративная версия факториала."""
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


assert factorial(0) == 1
assert factorial(5) == 120

for n in range(0, 21):
    assert factorial(n) == factorial_iterative(n), f"Несовпадение для n={n}"

print("Рекурсивная и итеративная версии совпадают для 0..20")

# Трассировка factorial(3):
# factorial(3) = 3 * factorial(2)
#              = 3 * (2 * factorial(1))
#              = 3 * (2 * (1 * factorial(0)))
#              = 3 * (2 * (1 * 1))
#              = 3 * (2 * 1)
#              = 3 * 2
#              = 6

