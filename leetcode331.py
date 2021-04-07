class Solution:

    def isValidSerialization(self, preorder: str) -> bool:
        stack = list()
        for i in preorder.split(','):
            stack.append(i)
            while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#' and stack[-3].isdigit():
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return True if stack == ['#'] else False

sv = Solution()
print(sv.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

