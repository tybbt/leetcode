import math
class Solution:

    def calculate(self, s: str) -> int:
        switch = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a / b}
        if s.isdigit():
            return int(s)
        stack = []
        s = s[::-1]
        numberstack = ""
        callbackflag = 0
        for l in s:
            if l == ' ':
                continue
            elif l.isdigit():
                numberstack = l+numberstack
            elif l == '+':
                stack.append(int(numberstack))
                if callbackflag:
                    while callbackflag != 0:
                        n1 = stack.pop()
                        op = stack.pop()
                        n2 = stack.pop()
                        rs = switch[op](n1, n2)
                        stack.append(rs)
                        callbackflag -= 1
                numberstack = ''
            elif l == '-':
                stack.append(int(numberstack))
                if callbackflag:
                    while callbackflag != 0:
                        n1 = stack.pop()
                        op = stack.pop()
                        n2 = stack.pop()
                        rs = switch[op](n1, n2)
                        stack.append(rs)
                        callbackflag -= 1
                c = stack.pop()
                stack.append(-c)
                numberstack = ''
            elif l == '*':
                stack.append(int(numberstack))
                callbackflag += 1
                stack.append(l)
                numberstack = ''
            elif l == '/':
                stack.append(int(numberstack))
                callbackflag += 1
                stack.append(l)
                numberstack = ''

        if numberstack != '':
            stack.append(int(numberstack))
        while callbackflag != 0:
            n1 = stack.pop()
            op = stack.pop()
            n2 = stack.pop()
            rs = switch[op](n1, n2)
            stack.append(rs)
            callbackflag -= 1
        return math.floor(sum(stack))

sv = Solution()
print(sv.calculate("5 / 2"))

