from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if target < matrix[0][0]:
            return False
        row = len(matrix)
        column = len(matrix[0])

        # return an potential row that target most probably in
        num_row = row-1
        while num_row:
            if target >= matrix[num_row][0]:
                break
            num_row -= 1

        # 二分查找
        def halfColumn(columnList, left, right) -> bool:
            if left == right:
                return target == columnList[left]
            mid = int(left + (right - left) / 2)
            if target < columnList[mid]:
                return halfColumn(columnList, left, mid)
            elif target > columnList[mid]:
                return halfColumn(columnList, mid + 1, right)
            else:
                return True

        return halfColumn(matrix[num_row], 0, column-1)


matrix = [[1],[3]]
target = 3
sv = Solution()
print(sv.searchMatrix(matrix, target))
