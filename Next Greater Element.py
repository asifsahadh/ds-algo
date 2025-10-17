def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      res = []
      for i in range(len(nums1)):
          idx_2 = nums2.index(nums1[i])
          if idx_2 + 1 == len(nums2): # last index
              res.append(-1)
          else:
              remaining = nums2[idx_2 + 1:]
              for ele in remaining:
                  if ele > nums2[idx_2]:
                      res.append(ele)
                      break
              else:
                  res.append(-1)
                  
      return res
