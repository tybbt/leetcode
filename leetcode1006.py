class Solution:
    def clumsy(self, N: int) -> int:
        # 用于计算的switch 0：乘法， 1：整除， 2：加法， 3：减法
        op = 0
        stack = [N]
        for i in range(0, N-1):
            N -= 1
            if op == 0:
                temp = stack.pop()
                temp *= N
                stack.append(temp)
            elif op == 1:
                temp = stack.pop()
                temp = int(temp/N)
                stack.append(temp)
            elif op == 2:
                stack.append(N)
            elif op == 3:
                stack.append(-N)
            op = (op + 1) % 4
        return sum(stack)

sv = Solution()
print(sv.clumsy(4))
