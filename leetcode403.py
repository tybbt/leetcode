from typing import List
class Solution:
    def canCross(stones: List[int]) -> bool:
        set_stones = set(stones)
        from collections import defaultdict
        dp = defaultdict(set)
        dp[0] = {0}
        for s in stones:
            for step in dp[s]:
                for d in [-1, 0, 1]:
                    if step + d > 0 and s + step + d in set_stones:
                        dp[s + step + d].add(step + d)
        return len(dp[stones[-1]]) > 0


sv = Solution()
stones = [0,1,3,5,6,8,12,17]
print(sv.canCross(stones))

