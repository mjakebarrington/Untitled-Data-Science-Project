# Some useful operations on matrices:


def m_shape(A):
    """
    Determines the shape of matrix A.
    """
    rows = len(A)
    columns = len(A[0]) if A else 0
    return rows, columns


def m_get_row(A, i):
    return A[i]


def m_get_column(A, j):
    return [A1[j] for A1 in A]


def m_make_matrix(number_rows, number_columns, entry_fn):
    """
    Returns a number_rows x number_columns matrix whose (i,j)th entry is entry_fn(i, j)
    """
    return [[entry_fn(i, j) for j in range(number_columns)] for i in range(number_rows)]


def m_diagonal(i, j):
    """
    Useful for creating identity matrix. When making matrix returns '1s' across diagonal.
    """
    return 1 if i == j else 0
