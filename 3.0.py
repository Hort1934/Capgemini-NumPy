import numpy as np


def print_array(array, message=''):
    if message:
        print(message)
    print(array)
    print('\n')


# 1. Array Creation:
# Generate a multi-dimensional NumPy array with random values. The array should have a complex structure (e.g., a 6x6 matrix of integers) to clearly demonstrate changes through each manipulation.

initial_array = np.random.randint(1, 100, size=(6, 6))


# 2. Array Manipulation Functions:
def transpose_array(array):
    return np.transpose(array)


def reshape_array(array, new_shape):
    return np.reshape(array, new_shape)


def split_array(array, sections, axis=0):
    return np.array_split(array, sections, axis=axis)


def combine_arrays(arrays, axis=0):
    return np.concatenate(arrays, axis=axis)


# 3. Manipulation Workflow:
def main():
    print_array(initial_array, "Initial 6x6 array:")

    transposed_array = transpose_array(initial_array)
    print_array(transposed_array, "Transposed array:")

    reshaped_array = reshape_array(initial_array, (3, 12))
    print_array(reshaped_array, "Reshaped array (3x12):")

    split_arrays = split_array(initial_array, 3, axis=0)
    for i, split_array_part in enumerate(split_arrays):
        print_array(split_array_part, f"Split array part {i + 1}:")

    combined_array = combine_arrays(split_arrays, axis=0)
    print_array(combined_array, "Combined array from split parts:")

    # Assertions to verify the dimensions and integrity of the array
    assert transposed_array.shape == (6, 6), "Transposed array shape mismatch"
    assert reshaped_array.shape == (3, 12), "Reshaped array shape mismatch"
    assert len(split_arrays) == 3, "Split arrays count mismatch"
    assert all(part.shape[1] == 6 for part in split_arrays), "Split arrays column count mismatch"
    assert combined_array.shape == initial_array.shape, "Combined array shape mismatch"


if __name__ == "__main__":
    main()
