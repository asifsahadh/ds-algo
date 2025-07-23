def singleNumber(self, nums: List[int]) -> int:
    for i in range(len(nums)):
        num_in_hand = nums.pop(i)
        if num_in_hand in nums:
            nums.insert(i, num_in_hand)
        else:
            return num_in_hand
