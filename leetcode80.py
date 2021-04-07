from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        index = 0
        while length and index < length:
            curNum = nums[index]
            count = nums.count(curNum)
            if count > 2:
                count -= 2
                length -= count
                while count:
                    nums.remove(curNum)
                    count -= 1

            else:
                index += 1

        return length


nums = [0,0,1,1,1,1,2,3,3]
sv = Solution()
print(sv.removeDuplicates(nums))
print(nums)
