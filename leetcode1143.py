class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        column = len(text1)+1
        row = len(text2)+1
        matrix = [[0 for _ in range(0,column)] for _ in range(0, row+1)]
        for i in range(1, row):
            for j in range(1, column):
                if text2[i-1] == text1[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]+1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        return matrix[i][j]


sv = Solution()
print(sv.longestCommonSubsequence('abcd', 'ac'))
