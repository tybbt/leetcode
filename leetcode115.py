class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # 构建动态规划矩阵
        row = len(t)  # 行数(除去空字符)
        column = len(s)  # 列数(除去空字符)
        matrix = [[0 for _ in range(0, column+1)] for _ in range(0, row+1)]
        for i in range(0, column + 1):
            matrix[0][i] = 1

        # 动态规划
        for i in range(1, row+1):
            for j in range(1, column+1):
                if s[j-1] == t[i-1]:
                    matrix[i][j] = matrix[i-1][j-1] + matrix[i][j-1]
                else:
                    matrix[i][j] = matrix[i][j-1]
        return matrix[row][column]

class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        ls = len(s)
        lt = len(t)
        a = [0] * lt + [1]
        for i in range(ls):
            for j in range(lt-1, -1, -1):
                if s[i]==t[j]:
                    a[j] += a[j-1]
                    print(a)
        return a[lt-1]



sv = Solution()
sv2 = Solution2()
print(sv.numDistinct("rabbbit", "rabbit"))
print(sv2.numDistinct("rabbbit", "rabbit"))
