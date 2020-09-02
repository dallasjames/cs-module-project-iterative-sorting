def linear_search(arr, target):
    for i in arr:
        if i == target:
            return arr.index(i)
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while end >= start:
        middle_index = (start + end) // 2
        middle_value = arr[middle_index]
        if target == middle_value:
            return arr.index(target)
        if target > middle_value:
            start = middle_index + 1
        if target < middle_value:
            end = middle_index - 1
    return -1   # not found
