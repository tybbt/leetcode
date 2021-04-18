from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        index_tag = 0
        current_duplicate_element = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != current_duplicate_element:
                index_tag += 1
                nums[index_tag] = nums[i]
                current_duplicate_element = nums[i]
        difference = len(nums) - index_tag - 1
        while difference:
            nums.pop()
            difference -= 1
        return len(nums)


sv = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(sv.removeDuplicates(nums))
print(nums)



