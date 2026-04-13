import numpy as np
import time


def create_data(size=1_000_000):
    """
    Create large datasets for comparison.
    """
    py_list = list(range(size))
    np_array = np.arange(size)
    return py_list, np_array


def python_list_operation(py_list):
    """
    Square each element using Python list (loop-based).
    """
    result = []
    for x in py_list:
        result.append(x * x)
    return result


def numpy_operation(np_array):
    """
    Square each element using NumPy (vectorized).
    """
    return np_array * np_array


def measure_time(func, data):
    """
    Measure execution time of a function.
    """
    start = time.time()
    func(data)
    end = time.time()
    return end - start


def main():
    py_list, np_array = create_data()

    print("Dataset size:", len(py_list))

    # Measure Python list performance
    py_time = measure_time(python_list_operation, py_list)

    # Measure NumPy performance
    np_time = measure_time(numpy_operation, np_array)

    print("\n--- Performance Comparison ---")
    print(f"Python List Time: {py_time:.6f} seconds")
    print(f"NumPy Array Time: {np_time:.6f} seconds")

    # Speedup calculation
    speedup = py_time / np_time if np_time > 0 else float('inf')
    print(f"NumPy is ~{speedup:.2f}x faster than Python lists")


    main()