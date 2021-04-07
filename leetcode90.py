from typing import List
class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        lengthNums = len(nums)
        def buildsubset(subset: List[List[int]], times: int):
            if times == 0:
                return
            sets = []
            length = len(subset)
            for i in range(0, length):
                temp = []
                temp.extend(nums)
                for l in subset[i]:
                    temp.remove(l)
                for l in temp:
                    new = []
                    new.extend(subset[i])
                    new.append(l)
                    new.sort()
                    if new not in subsets and new not in sets:
                        sets.append(new)
            times -= 1
            subsets.extend(sets)
            buildsubset(sets, times)
        for i in nums:
            c = []
            c.append(i)
            if c not in subsets:
                subsets.append(c)
        buildsubset(subsets, lengthNums-1)
        return subsets




sv = Solution()
print(sv.subsetsWithDup([1,2,2]))
