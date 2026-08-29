class Solution:
    def check(self, nums: List[int]) -> bool:
        # if nums == sorted(nums):
        #     return True
        # else:
        #     for i in nums:
        #         poped = nums.pop(i)
        #         nums.append(i)
        #         if nums == sorted(nums):
        #             return True
        #     else:
        #         return False count = 0
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1