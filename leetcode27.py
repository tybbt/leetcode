from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        index_tag = -1
        for i in range(0, len(nums)):
            if nums[i] == val:
                continue
            else:
                index_tag += 1
                nums[index_tag] = nums[i]

        return index_tag + 1


sv = Solution()
nums = [1]
val = 1
print(sv.removeElement(nums, val))
print(nums)
