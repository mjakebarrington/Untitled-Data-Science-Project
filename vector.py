# Some useful arithmetic functions on vectors
# I could have just used numpy, but what's the fun in that?
from functools import reduce
from math import sqrt


def v_add(v, w):
    """Performs componentwise addition on two vectors. Returns a list."""
    return [vi + wi for vi, wi in zip(v, w)]


def v_sub(v, w):
    """Performs componentwise subtraction on two vectors. Returns a list."""
    return [vi - wi for vi, wi in zip(v, w)]


def v_sum(vectors):
    """Componentwise summation of corresponding vector elements."""
    return reduce(v_add, vectors)


def s_v_m(c, v):
    """Performs scalar vector multiplication. c = number, v = vector"""
    return [c * vi for vi in v]


def v_mean(vectors):
    """Compute componentwise mean of a list of same sized vectors."""
    n = len(vectors)
    return s_v_m(1/n, v_sum(vectors))


def v_dot(v, w):
    """
    Computes dot product of two vectors:
    v1 * w1 + ... + vn * wn
    """
    # A measure of how far v extends in the w direction
    return sum(v1 * w1 for v1, w1 in zip(v, w))


def v_sum_sqrs(v):
    """
    Computes vector sum of squares
    v1 * v1 + ... + vn * vn
    """


def v_magnitude(v):
    """Computes magnitude of vector v"""
    return sqrt(v_sum_sqrs(v))

# The following are used to compute the distance between two vectors as defined (LaTeX):
# \sqrt{(v_1-w_1)^{2}+...+(v_n-w_n)^{2}}


def v_square_distance(v, w):
    """
    Returns the sum of the difference between corresponding elements in vectors v and w squared:
    (v1-w1) ** 2 + ... + (vn - wn) ** 2
    """
    return v_sum_sqrs(v_sub(v, w))


def v_distance(v, w):
    return sqrt(v_square_distance(v, w))
