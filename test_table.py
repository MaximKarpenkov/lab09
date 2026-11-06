from table import row_sums, column_sums, diagonal_pattern, transform

# Суммы строк и столбцов
m = [[1, 2, 3], [4, 5, 6]]
assert row_sums(m) == [6, 15]
assert column_sums(m) == [5, 7, 9]

# Один элемент
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

# Один столбец
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

# Пустая матрица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# Узор 3x3
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0],
]

# Вариант 1: контрольная матрица
control = [[-2, 0, 3], [4, -5, 6]]
expected = [[0, 0, 3], [4, 0, 6]]
assert transform(control) == expected

# Исходная матрица не изменяется
saved = [row.copy() for row in control]
transform(control)
assert control == saved

# Изменение результата не влияет на исходную матрицу
result = transform(control)
result[0][0] = 999
assert control == [[-2, 0, 3], [4, -5, 6]]

print("Все проверки пройдены")

