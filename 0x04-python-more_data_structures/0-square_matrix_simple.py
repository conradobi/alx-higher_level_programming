#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat_rix_copy = matrix[:]
    mat_rix = []
    for i in range(0, len(mat_rix_copy)):
        mat_rix.append([])
        for j in mat_rix_copy[i]:
            mat_rix[i].append(j**2)
    return mat_rix
