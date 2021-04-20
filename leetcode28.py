class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 or len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            if len(haystack) - i < len(needle):
                return -1
            if needle[0] == haystack[i] and haystack[i:i+len(needle)] == needle:
                return i
        return -1

sv = Solution()
haystack = "hello"
needle = "ll"
print(sv.strStr(haystack, needle))
