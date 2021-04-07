class Solution:
    def removeDuplicates(self, S):
        stack = ['']
        for i in S:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack[1:])
sv = Solution()
print(sv.removeDuplicates("abbbasdaba"))

