def transpose_matrix(matrix: list[list]) -> list[list]:
    transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


def rank_of_matrix(matrix: list[list]) -> int:
    rank = min(len(matrix), len(matrix[0]))
    row_index = 0
    for i in range(len(matrix[0])):
        found_nonzero = False
        for j in range(row_index, len(matrix)):
            if matrix[j][i] != 0:
                found_nonzero = True
                matrix[row_index], matrix[j] = matrix[j], matrix[row_index]
                break
        if found_nonzero:
            for j in range(row_index + 1, len(matrix)):
                factor = matrix[j][i] / matrix[row_index][i]
                for k in range(i, len(matrix[0])):
                    matrix[j][k] -= matrix[row_index][k] * factor
            row_index += 1
    return rank


def inverse_matrix(matrix: list[list]) -> list[list]:
    augmented_matrix = [
        [
            matrix[i][j] if j < len(matrix) else int(i == j - len(matrix))
            for j in range(2 * len(matrix))
        ]
        for i in range(len(matrix))
    ]
    for i in range(len(matrix)):
        pivot = augmented_matrix[i][i]
        if pivot == 0:
            raise ValueError("Matrix is not invertible")
        for j in range(2 * len(matrix)):
            augmented_matrix[i][j] /= pivot
        for j in range(len(matrix)):
            if i != j:
                scalar = augmented_matrix[j][i]
                for k in range(2 * len(matrix)):
                    augmented_matrix[j][k] -= scalar * augmented_matrix[i][k]
    inverse = [
        [augmented_matrix[i][j] for j in range(len(matrix), 2 * len(matrix))]
        for i in range(len(matrix))
    ]
    return inverse


def multiply_matrix(matrix: list[list], n: int) -> list[list]:
    result = []
    for i in matrix:
        new_row = []
        for j in i:
            new_element = j * n
            new_row.append(new_element)
        result.append(new_row)
    return result


def exponentiate_matrix(matrix: list[list], n: int) -> list[list]:
    if n < 0:
        raise ValueError("Exponent must be non-negative")
    result = [[int(i == j) for j in range(len(matrix))] for i in range(len(matrix))]
    for i in range(n):
        temp = []
        for j in range(len(matrix)):
            row = []
            for k in range(len(matrix)):
                element = 0
                for e in range(len(matrix)):
                    element += result[j][e] * matrix[e][k]
                row.append(element)
            temp.append(row)
        result = temp

    return result
