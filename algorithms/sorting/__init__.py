from typing import List


def quick(lst: List[int]) -> List[int]:
    """
    Quick Sort

    :param lst: A list of integers
    :return: A list of sorted integers
    """
    # Base case: if the list is one or zero items, it's already sorted
    if len(lst) <= 1:
        return lst

    # Choose a pivot point - in this case, the middle element of the list
    pivot = lst[len(lst) // 2]

    # Create three lists: one for elements less than the pivot, one for elements equal to the pivot,
    # and one for elements greater than the pivot
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    # Recursively sort the left and right lists, and combine the sorted lists and the middle list
    return quick(left) + middle + quick(right)


def selection(lst: List[int]) -> List[int]:
    """
    Selection Sort

    :param lst: A list of integers
    :return: A list of sorted integers
    """
    # Iterate over each element in the list
    for i in range(len(lst)):
        # Assume the current element is the smallest
        min_index = i
        # Iterate over the rest of the list to find if there's any element smaller than the current
        for j in range(i+1, len(lst)):
            # If a smaller element is found, update min_index
            if lst[j] < lst[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        lst[i], lst[min_index] = lst[min_index], lst[i]
    # Return the sorted list
    return lst


def insertion(lst: List[int]) -> List[int]:
    """
    Insertion Sort

    :param lst: A list of integers
    :return: A list of sorted integers
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    return lst