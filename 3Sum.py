class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ## BRUTE
        # final = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
        #                 if triplet not in final:
        #                     final.append(triplet)
        # return final

        ## OPTIM
        final = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # because triplets already looked for at i - 1

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    final.append([nums[i], nums[left], nums[right]])
                    
                    # duplicate handling
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return final
