from typing import List
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        height = len(wall)
        gap = [[] for _ in range(height)]
        row_i = 0
        for row in wall:
            gap_situation = 0
            for block in row[:-1]:
                gap_situation += block
                gap[row_i].append(gap_situation)
            row_i += 1
        maxgap = 0
        from collections import defaultdict
        di = defaultdict(int)
        for row in gap:
            for num in row:
                di[num] += 1
        for num in di.values():
            if maxgap < num:
                maxgap = num

        return height - maxgap



sv = Solution()
wall = [[1],[1],[1]]
print(sv.leastBricks(wall))

