from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        MIN = -float('inf')
        stack = []

        for n in nums[::-1]:
            if n < MIN:
                return True

            while stack and n > stack[-1]:
                MIN = max(MIN, stack.pop())

            stack.append(n)

        return False


sv = Solution()
print(sv.find132pattern([3,5,0,3,4]))


