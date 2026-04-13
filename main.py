import numpy as np
import time
from operations import create_dataset, mathematical_operations, axis_operations, statistical_operations
from reshape_broadcast import create_data, reshaping_examples, broadcasting_examples
from file_io import create_sample_data, save_npy, load_npy, save_npz, load_npz, save_txt, load_txt
from performance_compare import create_data as perf_create_data, python_list_operation, numpy_operation, measure_time


def array_creation():
    """
    Demonstrates different ways to create NumPy arrays.
    """

    # 1D Array
    arr1 = np.array([1, 2, 3, 4, 5])

    # 2D Array
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])

    # Zeros array
    zeros = np.zeros((2, 3))

    # Ones array
    ones = np.ones((2, 3))

    # Range array
    rng = np.arange(0, 10, 2)

    # Random array
    random_arr = np.random.rand(2, 3)

    return arr1, arr2, zeros, ones, rng, random_arr


def indexing_examples(arr):
    """
    Demonstrates indexing in NumPy arrays.
    """

    # Access single element
    first_element = arr[0]

    # Access last element
    last_element = arr[-1]

    return first_element, last_element


def slicing_examples(arr):
    """
    Demonstrates slicing operations.
    """

    # Slice first 3 elements
    first_three = arr[:3]

    # Slice last 3 elements
    last_three = arr[-3:]

    # Slice with step
    step_slice = arr[::2]

    return first_three, last_three, step_slice


def main():
    # Array creation
    arr1, arr2, zeros, ones, rng, random_arr = array_creation()

    print("1D Array:", arr1)
    print("2D Array:\n", arr2)
    print("Zeros:\n", zeros)
    print("Ones:\n", ones)
    print("Range:", rng)
    print("Random:\n", random_arr)

    print("\n--- Indexing ---")
    first, last = indexing_examples(arr1)
    print("First element:", first)
    print("Last element:", last)

    print("\n--- Slicing ---")
    first3, last3, step = slicing_examples(arr1)
    print("First 3:", first3)
    print("Last 3:", last3)
    print("Step slice:", step)


    # -------------------------------
    # 1. Mathematical + Statistical
    # -------------------------------
    data = create_dataset()
    print("\nDataset:\n", data)

    add, sub, mul, div, sq, root = mathematical_operations(data)
    print("\nSquare:\n", sq)

    col_sum, row_sum, col_mean, row_mean = axis_operations(data)
    print("\nColumn Mean:", col_mean)

    mean, median, std, var, min_v, max_v = statistical_operations(data)
    print("\nMean:", mean)

    # -------------------------------
    # 2. Reshaping & Broadcasting
    # -------------------------------
    data1 = create_data()
    r2d, r3d, flat, auto = reshaping_examples(data1)

    print("\nReshaped 2D:\n", r2d)

    matrix, vector, b_add, s_add = broadcasting_examples()
    print("\nBroadcast Result:\n", b_add)

    # -------------------------------
    # 3. File I/O
    # -------------------------------
    arr1, arr2 = create_sample_data()

    save_npy(arr1)
    print("\nLoaded NPY:", load_npy())

    save_npz(arr1, arr2)
    l1, l2 = load_npz()
    print("Loaded NPZ:", l1)

    save_txt(arr1)
    print("Loaded TXT:", load_txt())

    # -------------------------------
    # 4. Performance Comparison
    # -------------------------------
    py_list, np_array = perf_create_data()

    py_time = measure_time(python_list_operation, py_list)
    np_time = measure_time(numpy_operation, np_array)

    print("\nPerformance:")
    print(f"Python List: {py_time:.6f}")
    print(f"NumPy: {np_time:.6f}")
    print(f"Speedup: {py_time / np_time:.2f}x")



if __name__ == "__main__":
    main()