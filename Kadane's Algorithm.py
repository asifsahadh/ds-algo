class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # BRUTE
        # sums = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums) + 1):
        #         sums.append(sum(nums[i:j]))
        # return max(sums)

        # OPTIM
        maxi = nums[0]
        curr_maxi = nums[0]

        for i in range(1, len(nums)):
            curr_maxi = max(nums[i], curr_maxi + nums[i])
            if curr_maxi > maxi:
                maxi = curr_maxi
        return maxi
