from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0 or c == 1:
            return True
        sq_c = round(sqrt(c))+1
        for a in range(sq_c):
            if a ** 2 > c:
                break
            b = int(sqrt(c-a**2))
            if a**2 + b**2 == c:
                return True
        return False




sv = Solution()
print(sv.judgeSquareSum(1000000000003))