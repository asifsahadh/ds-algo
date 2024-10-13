# Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. (Expected: Single pass-O(N) and constant space)

def sort(arr):
    
    zero_count = one_count = two_count = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            zero_count += 1

    for i in range(len(arr)):
        if arr[i] == 1:
            one_count += 1

    for i in range(len(arr)):
        if arr[i] == 2:
            two_count += 1

    for i in range(zero_count):
        arr[i] = 0    

    for i in range(one_count):
        arr[zero_count + i] = 1 

    for i in range(two_count):
        arr[zero_count + one_count + i] = 2
    
    return arr