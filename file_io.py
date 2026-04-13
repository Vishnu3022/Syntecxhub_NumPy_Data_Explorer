import numpy as np


def create_sample_data():
    """
    Create sample arrays for saving/loading.
    """
    arr1 = np.arange(10)
    arr2 = np.random.rand(3, 3)
    return arr1, arr2


def save_npy(arr):
    """
    Save a single NumPy array in binary format (.npy).
    """
    np.save("array_data.npy", arr)


def load_npy():
    """
    Load a NumPy array from .npy file.
    """
    return np.load("array_data.npy")


def save_npz(arr1, arr2):
    """
    Save multiple arrays into a single compressed file (.npz).
    """
    np.savez("multiple_arrays.npz", array1=arr1, array2=arr2)


def load_npz():
    """
    Load multiple arrays from .npz file.
    """
    data = np.load("multiple_arrays.npz")
    return data["array1"], data["array2"]


def save_txt(arr):
    """
    Save array as a text file.
    """
    np.savetxt("array.txt", arr, fmt="%d")


def load_txt():
    """
    Load array from a text file.
    """
    return np.loadtxt("array.txt")


def main():
    arr1, arr2 = create_sample_data()

    print("Original Array 1:", arr1)
    print("Original Array 2:\n", arr2)

    print("\n--- Saving & Loading (.npy) ---")
    save_npy(arr1)
    loaded_arr = load_npy()
    print("Loaded Array:", loaded_arr)

    print("\n--- Saving & Loading (.npz) ---")
    save_npz(arr1, arr2)
    l1, l2 = load_npz()
    print("Loaded Array 1:", l1)
    print("Loaded Array 2:\n", l2)

    print("\n--- Saving & Loading (Text) ---")
    save_txt(arr1)
    txt_arr = load_txt()
    print("Loaded from text:", txt_arr)


