def selection(lst):

    l = len(lst)
    for i in range(0, l):
        min_idx = i
        for j in range(i + 1, l):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]
        
    return lst