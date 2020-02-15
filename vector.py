# Some useful arithmetic functions on vectors
from functools import reduce

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