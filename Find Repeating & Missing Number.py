# You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

def repeating_missing(nums):
    
    # to find the repeating number
    seen = []
    for num in nums:
        if num in seen:
            rep = num
        else:
            seen.append(num)
    
    # to find the missing number
    l = len(nums)
    for i in range(1, l + 1):
        if i in nums:
            continue
        else:
            miss = i
    
    return(rep, miss)
