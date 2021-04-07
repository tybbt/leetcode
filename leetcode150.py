from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        switch = {'+': lambda a,b: a+b, '-': lambda a,b: a-b, '*': lambda a, b: a*b, '/': lambda a,b:int(a/b)}
        stack = []
        for l in tokens:
            if l.isdigit():
                stack.append(int(l))
            elif len(l) > 1 and l[0] == '-':
                stack.append(int(l))
            else:
                b = stack.pop()
                a = stack.pop()
                rs = switch[l](a, b)
                stack.append(rs)
        return stack.pop()


sv = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sv.evalRPN(tokens))

