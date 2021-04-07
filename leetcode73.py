from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        if row == 0:
            return
        column = len(matrix[0])

        # 保存第一行和第一列的0元素信息
        flag = [1, 1]   # 表示第一行，第一列  是否有0
        for i in range(0, column):
            if matrix[0][i] == 0:
                flag[0] = 0 # 行需置0
                break
        for j in range(0, row):
            if matrix[j][0] == 0:
                flag[1] = 0 # 列需置0
                break

        # 使用第一行第一列表示该行或该列是否有0
        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根据第一行第一列先把 m-1 * n-1 中的行列置0
        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, column):
                    matrix[i][j] = 0
        for j in range(1, column):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0

        # 根据情况将第一行第一列置0
        if flag[0] == 0:
            for j in range(0, column):
                matrix[0][j] = 0
        if flag[1] == 0:
            for i in range(0, row):
                matrix[i][0] = 0



matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
sv = Solution()
sv.setZeroes(matrix)
print(matrix)

