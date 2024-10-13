# Merge two sorted integer arrays, nums1 and nums2, into a single sorted array stored in nums1, with nums1 having extra space to accommodate all elements.

def merge(nums1, nums2, m, n):
    
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    nums1[:p2 + 1] = nums2[:p2 + 1]
        
    return nums1

merge(nums1, nums2, m, n)