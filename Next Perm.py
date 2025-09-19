class Solution(object):
    def nextPermutation(self, nums):

        l = len(nums)
        break_point = -1

        for i in range(l - 1):
            if nums[i] < nums[i + 1]: # basically find where there is an increase
                break_point = i
        
        if break_point == -1:
            return nums.reverse() # i didn't even know this was a thing
        
        # next, find the number index to the right of break_point which is larger that nums[break_point]
        next_big_thing = -1
        for i in range(break_point + 1, l):
            if nums[break_point] < nums[i]: 
                next_big_thing = i
        
        # swap
        nums[break_point], nums[next_big_thing] = nums[next_big_thing], nums[break_point]

        # rev
        nums[break_point + 1:] = reversed(nums[break_point + 1:])
