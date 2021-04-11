class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 0:
            return 0
        uglyList = [1]
        num_1, index_2 = 1, 0
        num_2, index_3 = 1, 0
        num_3, index_5 = 1, 0

        while len(uglyList) <= n:
            num_1 = uglyList[index_2] * 2
            num_2 = uglyList[index_3] * 3
            num_3 = uglyList[index_5] * 5
            if num_1 <= num_2 and num_1 <= num_3:
                index_2 += 1
                if num_1 not in uglyList:
                    uglyList.append(num_1)
            elif num_2 <= num_1 and num_2 <= num_3:
                index_3 += 1
                if num_2 not in uglyList:
                    uglyList.append(num_2)
            elif num_3 <= num_1 and num_3 < num_2:
                index_5 += 1
                if num_3 not in uglyList:
                    uglyList.append(num_3)
        return uglyList[n-1]

sv = Solution()
print(sv.nthUglyNumber(1))
