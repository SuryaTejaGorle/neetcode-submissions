class Solution:

    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)

        # x can only range from 1 to n
        for x in range(1, n + 1):
            # Count how many numbers are greater than or equal to x
            count = sum(1 for num in nums if num >= x)
            if count == x:
                return x

        return -1