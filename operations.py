import numpy as np


def create_dataset():
    """
    Create a sample dataset (2D array) for operations.
    Rows = samples
    Columns = features
    """
    np.random.seed(42)  # reproducibility
    data = np.random.randint(1, 100, size=(5, 4))  # 5x4 dataset
    return data


def mathematical_operations(data):
    """
    Perform element-wise mathematical operations.
    """

    addition = data + 10
    subtraction = data - 5
    multiplication = data * 2
    division = data / 2

    # Advanced operations
    square = np.square(data)
    sqrt = np.sqrt(data)

    return addition, subtraction, multiplication, division, square, sqrt


def axis_operations(data):
    """
    Perform operations along rows and columns.
    axis=0 → column-wise
    axis=1 → row-wise
    """

    # Sum
    col_sum = np.sum(data, axis=0)
    row_sum = np.sum(data, axis=1)

    # Mean
    col_mean = np.mean(data, axis=0)
    row_mean = np.mean(data, axis=1)

    return col_sum, row_sum, col_mean, row_mean


def statistical_operations(data):
    """
    Perform statistical analysis.
    """

    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    variance = np.var(data)

    min_val = np.min(data)
    max_val = np.max(data)

    return mean, median, std_dev, variance, min_val, max_val


def main():
    data = create_dataset()

    print("Dataset:\n", data)

    print("\n--- Mathematical Operations ---")
    add, sub, mul, div, sq, root = mathematical_operations(data)
    print("Add 10:\n", add)
    print("Multiply by 2:\n", mul)
    print("Square:\n", sq)

    print("\n--- Axis-wise Operations ---")
    col_sum, row_sum, col_mean, row_mean = axis_operations(data)
    print("Column Sum:", col_sum)
    print("Row Sum:", row_sum)
    print("Column Mean:", col_mean)
    print("Row Mean:", row_mean)

    print("\n--- Statistical Operations ---")
    mean, median, std, var, min_v, max_v = statistical_operations(data)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std)
    print("Variance:", var)
    print("Min:", min_v)
    print("Max:", max_v)


