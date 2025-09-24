class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # BRUTE
        # if len(nums) == 1:
        #     return nums[-1]
        # final = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums) + 1):
        #         prod = 1
        #         sub = nums[i:j]
        #         for ele in sub:
        #             prod *= ele 
        #         if final == []:
        #             final.append(prod)
        #         elif prod > final[-1]:
        #             final.pop(0)
        #             final.append(prod)
        # return final[-1]

        # OPTIM
        pre = 1
        suf = 1
        res = float('-inf')
        n = len(nums)

        for i in range(n):
            pre *= nums[i]
            suf *= nums[n - 1 - i]
            res = max(res, pre, suf)
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
                
        return res
