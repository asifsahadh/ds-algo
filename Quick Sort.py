def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high) # return pivot index
        quick_sort(arr, low, pivot - 1) # quick sort left of pivot index
        quick_sort(arr, pivot + 1, high) # quick sort right of pivot index
        
def partition(arr, low, high):
    p = arr[low] # let the pivot value be the lowest element (can be anything)
    i = low + 1 # for first iteration, this wil be 1
    j = high # for first iteration, this will be len(arr)
    while True:
        while i <= j and arr[i] <= p: # as long as index of i is lesser than j and value of i is lesser than pivot
            i += 1 # move right
        while i <= j and arr[j] >= p: # as long as index of i is lesser than j and value of j is greater than pivot
            j -= 1 # move left
        # we do this so that eventually, all the smaller elements will be to the left and the larger elements will be to the right of p
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] # atp, we swap the values
        else:
            break # we stop when i and j have crossed
    arr[low], arr[j] = arr[j], arr[low] # swap pivot(low) and j value
    return j