# Basic statistical functions
from math import sqrt
from vector import v_dot


def mean(x):
    """Finds mean value of data set x"""
    return sum(x) / len(x)


def median(x):
    """Finds the median value of data set x"""
    x_sorted = sorted(x)
    mid = len(x) // 2

    if len(x) % 2 == 1:
        return x_sorted[mid]

    else:
        l = mid - 1
        h = mid
        return (x_sorted[l] + x_sorted[h]) / 2


def quantile(x, p=0.50):
    """Returns the pth percentile value in x. Defaults to 50th percentile."""
    # Eg x, 0.10 returns 10th percentile value.
    pindex = int(p * len(x))
    return sorted(x)[pindex]


def data_range(x):
    """Computes the difference between the maximum and minimum elements of x."""
    return max(x) - min(x)


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x, sd = 'population'):
    """Computes variance (sigma squared) of x"""
    # Originally was going to borrow from vector, but I think its better standalone in stats.
    diff_elem_mean = [(elem - mean(x)) ** 2 for elem in x]
    if sd == 'sample':
        return sum(diff_elem_mean) / len(diff_elem_mean) - 1
    else:
        return mean(diff_elem_mean)


def std_deviation(x, sd = 'population'):
    """
    Finds the standard deviation of x. Assumes len(x) >= 2.
    sd = 'sample' for sample calculation
    """
    if sd == 'sample':
        return sqrt(variance(x, sd='sample'))
    else:
        return sqrt(variance(x))


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


def covariance(x, y):
    n = len(x)
    return v_dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    # 1 = perfect correlation, -1 perfect anticorrelation
    stdvx = std_deviation(x)
    stdvy = std_deviation(y)
    if stdvx > 0 and stdvy > 0:
        return covariance(x, y) / stdvx / stdvy
    else:
        return 0
