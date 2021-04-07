class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)
        strBin = str(binary)
        strBin = strBin[2:]
        length = len(strBin)
        while length != 32:
            strBin = '0'+strBin
            length += 1
        strBin = strBin[::-1]
        return int('0b'+strBin, 2)



sv = Solution()
print(sv.reverseBits(0b00000010100101000001111010011100))
