def row_sums(matrix):
    """Возвращает список сумм строк. Для [] возвращает []."""
    result = []
    for row in matrix:
        result.append(sum(row))
    return result


def column_sums(matrix):
    """Возвращает список сумм столбцов. Для [] возвращает []."""
    if not matrix:
        return []
    columns = len(matrix[0])
    result = [0] * columns
    for row in matrix:
        for index, value in enumerate(row):
            result[index] += value
    return result


def diagonal_pattern(size):
    """Квадратная таблица: на главной диагонали 0, выше — 1, ниже — 2."""
    matrix = []
    for row in range(size):
        new_row = []
        for column in range(size):
            if row == column:
                new_row.append(0)
            elif row < column:
                new_row.append(1)
            else:
                new_row.append(2)
        matrix.append(new_row)
    return matrix


def transform(matrix):
    """Вариант 1: отрицательные заменить нулями. Возвращает новую матрицу."""
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if value < 0:
                new_row.append(0)
            else:
                new_row.append(value)
        result.append(new_row)
    return result

