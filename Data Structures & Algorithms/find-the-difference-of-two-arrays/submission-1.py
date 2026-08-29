class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr = []
        arr1 = []
        new = []
        new1 = []

        for i in nums1:
            if i in nums2:
                continue
            else:
                arr.append(i)
        for i in arr:
            if i not in new:
                new.append(i)
        
        for j in nums2:
            if j in nums1:
                continue
            else:
                arr1.append(j)
        for i in arr1:
            if i not in new1:
                new1.append(i)

        return  [new] + [new1]
