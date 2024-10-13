# Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers. If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

def next_perm(arr):

    # 1
    k = -1
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            k = i
    if k == -1:
        arr.reverse()
        return arr

    # 2
    for i in range(len(arr) - 1, k, -1):
        if arr[i] > arr[k]:
            l = i
            break

    # 3
    temp2 = array[k]
    array[k] = array[l]
    array[l] = temp2

    # 4
    arr[k + 1:] = arr[k + 1:][::-1]

    return arr