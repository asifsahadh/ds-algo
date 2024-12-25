def insertion(lst):
    # insertion

    l = len(lst)
    for i in range(1, l):
        key = lst[i]
        j = i - 1
        while key < lst[j] and j >= 0:
            lst[j + 1] = lst[j]  
            j -= 1
        lst[j + 1] = key
        
    return lst