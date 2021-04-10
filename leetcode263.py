class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        def mod(num: int) -> bool:
            if num % 2 == 0:
                num /= 2
                return mod(num)
            elif num % 3 == 0:
                num /= 3
                return mod(num)
            elif num % 5 == 0:
                num /= 5
                return mod(num)
            elif num == 1:
                return True
            return False
        return mod(n)

sv = Solution()
print(sv.isUgly(0))
