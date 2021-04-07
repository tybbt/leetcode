from typing import List
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        sum = 0
        length = len(answers)
        while length:
            num = answers[0]
            count = answers.count(num)
            move = 1
            if count >= num+1:
                move = num + 1
            else:
                move = count
            sum += (num + 1)
            length -= move
            while move:
                answers.remove(num)
                move -= 1
        return sum



sv = Solution()
print(sv.numRabbits([1,1,2]))
