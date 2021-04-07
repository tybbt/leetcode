from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0
        maxHeight = max(height)

        def makeBinaryList(h: List[int]) -> int:
            s = ''
            for l in h:
                if l > 0:
                    s += '0'
                else:
                    s += '1'
            ls = list(s.strip('1'))
            return ls.count('1')

        rs = 0
        while maxHeight:
            new = makeBinaryList(height)
            rs += new
            maxHeight -= 1
            height[:] = [x-1 for x in height]
        return rs

    def trap2(self, height: List[int]) -> int:
        leftmax = [0]
        rightmax = [0]
        length = len(height)
        if length == 0:
            return 0
        co = height.copy()
        for i in range(1, length):
            t = co[i-1]-co[i]
            if t > 0:
                leftmax.append(t)
                co[i] = co[i-1]
            else:
                leftmax.append(0)
        co = height.copy()
        for j in range(length-2, -1, -1):
            t = co[j+1] - co[j]
            if t > 0:
                rightmax.insert(0,t)
                co[j] = co[j+1]
            else:
                rightmax.insert(0,0)
        stack = []
        for i in range(0, length-1):
            stack.append(min(leftmax[i], rightmax[i]))
        return sum(stack)





sv = Solution()
print(sv.trap2([4,2,3]))
