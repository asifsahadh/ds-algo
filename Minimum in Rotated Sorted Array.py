class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using binary search
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]: # pivot is on the right (init)
                low = mid + 1
            else: # pivot is on the left (init)
                high = mid
        return nums[high]
