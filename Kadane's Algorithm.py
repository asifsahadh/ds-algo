# Given an integer array arr, find the contiguous subarray (containing at least one number) which has the largest sum and returns its sum and prints the subarray.

# brute force

def kadane(arr):
    temp = []
    l = len(arr)
    
    for i in range(l):
        s = 0
        for j in range(i, l):
            s += arr[j]
            temp.append(s)
            
    return max(temp)

# better solution

def kadane_bet(arr):
    maxi = arr[0]
    cur_maxi = arr[0]
    for i in range(1, len(arr)):
        cur_maxi = max(arr[i], cur_maxi + arr[i])
        if cur_maxi > maxi:
            maxi = cur_maxi
    return maxi

# note: space/time complexities are better by a mile for the second solution
