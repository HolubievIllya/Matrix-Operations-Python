def read_matrix_from_file(file_path):
    with open(file_path, "r") as file:
        matrix = [[int(num) for num in line.split()] for line in file]
    return matrix
