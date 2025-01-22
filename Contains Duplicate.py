# given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):

    # brute force
    # seen = []
    # for num in nums:
    #     if num in seen:
    #         return True
    #         break
    #     seen.append(num)
    # return False
    
    # sorting and comparing
    sorted_nums = sorted(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1]:
            return True
            break
    return False