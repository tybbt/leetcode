from typing import List

"O(M*N)"
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        column = len(matrix[0])
        element = row * column
        spiral = []
        while row != 1 and column != 1 and element != 0:
            spiral.extend(matrix[0])
            matrix.pop(0)
            row -= 1
            for l in matrix:
                last = l.pop(len(l)-1)
                spiral.append(last)
            column -= 1
            spiral.extend(matrix[row-1][::-1])
            matrix.pop(row-1)
            row -= 1
            for l in matrix[::-1]:
                first = l.pop(0)
                spiral.append(first)
            column -= 1
            element = row * column
        if row == 1:
            spiral.extend(matrix[0])
        elif column == 1:
            for l in matrix:
                spiral.append(l.pop())
        return spiral

matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
sv = Solution()
print(sv.spiralOrder(matrix))
