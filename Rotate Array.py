def rotate(self, nums: List[int], k: int) -> None:
    c = 0
    while c < k:
        temp = nums.pop()
        nums.insert(0, temp)
        c += 1
    return nums
