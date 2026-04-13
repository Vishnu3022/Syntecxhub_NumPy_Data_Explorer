import numpy as np


def create_data():
    """
    Create base dataset for reshaping and broadcasting.
    """
    data = np.arange(1, 13)  # 1 to 12
    return data


def reshaping_examples(data):
    """
    Demonstrates reshaping techniques.
    """

    # Convert 1D → 2D
    reshaped_2d = data.reshape(3, 4)

    # Convert 1D → 3D
    reshaped_3d = data.reshape(2, 2, 3)

    # Flatten back to 1D
    flattened = reshaped_2d.flatten()

    # Reshape using -1 (auto dimension)
    auto_reshape = data.reshape(2, -1)

    return reshaped_2d, reshaped_3d, flattened, auto_reshape


def broadcasting_examples():
    """
    Demonstrates broadcasting rules.
    """

    # 2D array
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6]])

    # 1D array
    vector = np.array([10, 20, 30])

    # Broadcasting: vector added to each row
    broadcast_add = matrix + vector

    # Scalar broadcasting
    scalar_add = matrix + 5

    return matrix, vector, broadcast_add, scalar_add


def advanced_broadcasting():
    """
    Column-wise broadcasting example.
    """

    matrix = np.array([[1, 2, 3],
                       [4, 5, 6]])

    column_vector = np.array([[10],
                              [20]])

    # Broadcasting column-wise
    result = matrix + column_vector

    return matrix, column_vector, result


def main():
    data = create_data()

    print("Original Data:", data)

    print("\n--- Reshaping ---")
    r2d, r3d, flat, auto = reshaping_examples(data)
    print("2D:\n", r2d)
    print("3D:\n", r3d)
    print("Flatten:", flat)
    print("Auto reshape:\n", auto)

    print("\n--- Broadcasting (Row-wise) ---")
    matrix, vector, b_add, s_add = broadcasting_examples()
    print("Matrix:\n", matrix)
    print("Vector:", vector)
    print("Broadcast Add:\n", b_add)
    print("Scalar Add:\n", s_add)

    print("\n--- Broadcasting (Column-wise) ---")
    mat, col_vec, result = advanced_broadcasting()
    print("Matrix:\n", mat)
    print("Column Vector:\n", col_vec)
    print("Result:\n", result)


if __name__ == "__main__":
    main()