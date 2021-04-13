from typing import List
class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        key = cmp_to_key(lambda x,y: int(y+x)-int(x+y))
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'

nums = [3,30,34,5,9]
sv = Solution()
print(sv.largestNumber(nums))

