# Write a function that takes in an array and sorts it from smallest to largest and returns the sorted array

array = [3, 6, 1, 6, 3, 5]


def bubble_sort(arr):
    i = 0
    j = 0

    # nested for loop is used since we need to go through the array multiple times to run checks on each list position to make sure all max values are pushed to the right.

    for i in range(len(arr) - 1):
        # need to take 1 off the length since we are evaluating j + 1. If not, we would have index out of range error because we would evaluate an index on the list that does not exist in our array.

        for j in range(len(arr) - 1):

            if arr[j] < arr[j+1]:
                pass
            # Learned how to do this python shorthand trick to switch variables without using a temporary one.
            else:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


sorted_array = bubble_sort(array)
print(sorted_array)
