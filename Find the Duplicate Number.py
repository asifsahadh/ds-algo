# Given an array of N + 1 size, where each element is between 1 and N. Assuming there is only one duplicate number, your task is to find the duplicate number.

# brute force

def find_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:              
                return nums[i]

# better solution (floyd's tortoise & hare)

def find_duplicate(nums):
    
    tortoise = hare = nums[0]
    
    while True:
        tortoise = nums[tortoise]
        hare = nums[hare]
        if tortoise == hare:
            break

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return tortoise