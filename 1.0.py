import numpy as np


def print_array(array, message=''):
    if message:
        print(message)
    print(array)


def main():
    # 1. Array Creation:
    # Create a one-dimensional NumPy array with values ranging from 1 to 10
    first_array = np.arange(1,11)
    print_array(first_array, "\nOne-dimensional array with values from 1 to 10:")

    # Create a two-dimensional NumPy array (matrix) with shape (3, 3) containing values from 1 to 9.
    second_array = np.arange(1,10).reshape(3,3)
    print_array(second_array, "\nTwo-dimensional array (3x3) with values from 1 to 9:")

    # 2. Basic Operations:
    # Indexing and Slicing:
    # Access and print the third element of the one-dimensional array.
    third_array = first_array[2]
    print_array(third_array, "\nThird element of the one-dimensional array:")

    # Slice and print the first two rows and columns of the two-dimensional array.
    sliced_second_array = second_array[:2, :2]
    print_array(sliced_second_array, "\nFirst two rows and columns of the two-dimensional array:")

    # Basic Arithmetic:
    # Add 5 to each element of the one-dimensional array and print the result.
    first_array_plus = first_array + 5
    print_array(first_array_plus, "\nOne-dimensional array after adding 5 to each element:")

    # Multiply each element of the two-dimensional array by 2 and print the result.
    second_array_multiply = second_array * 2
    print_array(second_array_multiply, "\nTwo-dimensional array after multiplying each element by 2:")


if __name__ == '__main__':
    main()