from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        MIN = nums[0]
        length = len(nums)
        r, l = 0, length-1
        while r <= l:
            MIN = min(nums[r], nums[l], MIN)
            r += 1
            l -= 1
        return MIN

sv = Solution()
print(sv.findMin([3,1,3]))
