# Basic statistical functions
import vector

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

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return vector.v_sum_sqrs(deviations) / (n - 1)