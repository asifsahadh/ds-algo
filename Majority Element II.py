class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # # BRUTE
        # co = len(nums) // 3
        # unique = list(set(nums))
        # d = dict()
        # for num in unique:
        #     c = nums.count(num)
        #     d[num] = c
        # f = []
        # for k, v in d.items():
        #     if v > co:
        #         f.append(k)
        # return f

        # OPTIM
        seen = dict()
        fin = []
        co = len(nums) // 3
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
            if seen[num] > co:
                fin.append(num)
        return list(set(fin))
