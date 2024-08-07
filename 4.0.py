import numpy as np


def print_array(array, message=''):
    if message:
        print(message)
    print(array)
    print('\n')


# 1. Array Creation:
# Generate a multi-dimensional NumPy array with random values. The array should have a complex structure (e.g., a 10x10 matrix of integers) to clearly demonstrate changes through each manipulation.

initial_array = np.random.randint(1, 100, size=(10, 10))


# 2. Data I/O Functions:
def save_array(array, filename_prefix):
    np.savetxt(f"{filename_prefix}.txt", array, fmt='%d')
    np.savetxt(f"{filename_prefix}.csv", array, delimiter=',', fmt='%d')
    np.save(f"{filename_prefix}.npy", array)
    np.savez(f"{filename_prefix}.npz", array)


def load_array(filename_prefix):
    array_txt = np.loadtxt(f"{filename_prefix}.txt", dtype=int)
    array_csv = np.loadtxt(f"{filename_prefix}.csv", delimiter=',', dtype=int)
    array_npy = np.load(f"{filename_prefix}.npy")
    array_npz = np.load(f"{filename_prefix}.npz")['arr_0']
    return array_txt, array_csv, array_npy, array_npz


# 3. Aggregate Functions:
def sum_array(array):
    return np.sum(array)


def mean_array(array):
    return np.mean(array)


def median_array(array):
    return np.median(array)


def std_array(array):
    return np.std(array)


def sum_axis(array, axis):
    return np.sum(array, axis=axis)


def mean_axis(array, axis):
    return np.mean(array, axis=axis)


def median_axis(array, axis):
    return np.median(array, axis=axis)


def std_axis(array, axis):
    return np.std(array, axis=axis)


# 5. Manipulation Workflow:
def main():
    print_array(initial_array, "Initial 10x10 array:")

    # Save the array in different formats
    save_array(initial_array, 'array_data')

    # Load the arrays back from the saved files
    array_txt, array_csv, array_npy, array_npz = load_array('array_data')

    # Verify the integrity of the loaded arrays
    print_array(array_txt, "Array loaded from text file:")
    print_array(array_csv, "Array loaded from CSV file:")
    print_array(array_npy, "Array loaded from NPY file:")
    print_array(array_npz, "Array loaded from NPZ file:")

    assert np.array_equal(initial_array, array_txt), "Loaded array from text file does not match the original"
    assert np.array_equal(initial_array, array_csv), "Loaded array from CSV file does not match the original"
    assert np.array_equal(initial_array, array_npy), "Loaded array from NPY file does not match the original"
    assert np.array_equal(initial_array, array_npz), "Loaded array from NPZ file does not match the original"

    # Compute and print aggregate functions
    total_sum = sum_array(initial_array)
    print(f"Total Sum: {total_sum}")

    mean_value = mean_array(initial_array)
    print(f"Mean Value: {mean_value}")

    median_value = median_array(initial_array)
    print(f"Median Value: {median_value}")

    std_value = std_array(initial_array)
    print(f"Standard Deviation: {std_value}")

    sum_rows = sum_axis(initial_array, axis=1)
    print_array(sum_rows, "Sum of each row:")

    sum_cols = sum_axis(initial_array, axis=0)
    print_array(sum_cols, "Sum of each column:")

    mean_rows = mean_axis(initial_array, axis=1)
    print_array(mean_rows, "Mean of each row:")

    mean_cols = mean_axis(initial_array, axis=0)
    print_array(mean_cols, "Mean of each column:")

    median_rows = median_axis(initial_array, axis=1)
    print_array(median_rows, "Median of each row:")

    median_cols = median_axis(initial_array, axis=0)
    print_array(median_cols, "Median of each column:")

    std_rows = std_axis(initial_array, axis=1)
    print_array(std_rows, "Standard deviation of each row:")

    std_cols = std_axis(initial_array, axis=0)
    print_array(std_cols, "Standard deviation of each column:")


if __name__ == "__main__":
    main()
