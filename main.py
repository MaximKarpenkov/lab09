from table import row_sums, column_sums, diagonal_pattern, transform


def read_matrix():
    """Ввод прямоугольной матрицы с проверкой длины строк."""
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def main():
    # 1. Ввод матрицы
    matrix = read_matrix()

    # 2. Суммы строк и столбцов
    print(f"Суммы строк: {row_sums(matrix)}")
    print(f"Суммы столбцов: {column_sums(matrix)}")

    # 3. Диагональный узор
    size = int(input("Размер квадратной таблицы: "))
    while size < 1:
        size = int(input("Размер должен быть >= 1: "))
    pattern = diagonal_pattern(size)
    print("Диагональный узор:")
    for row in pattern:
        print(*row)

    # 4. Преобразование (вариант 1)
    new_matrix = transform(matrix)
    print("Исходная матрица:")
    for row in matrix:
        print(*row)
    print("Новая матрица (отрицательные → 0):")
    for row in new_matrix:
        print(*row)


if __name__ == "__main__":
    main()

