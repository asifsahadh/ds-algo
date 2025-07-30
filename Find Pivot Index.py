def pivotIndex(self, nums: List[int]) -> int:
    t = sum(nums)
    cumsum = 0
    for i in range(len(nums)):
        cumsum += nums[i]
        if cumsum == t:
            return i
        t -= nums[i]
    return -1
