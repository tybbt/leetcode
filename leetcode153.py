from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        MIN = nums[0]
        l, r = 0, length-1

        while l <= r:
            MIN = min(nums[l], nums[r], MIN)
            l += 1
            r -= 1
        return MIN