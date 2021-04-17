from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        distance = k
        for i in range(0, len(nums)):
            if i + distance >= len(nums):
                k = len(nums) - 1 - i
                distance = k
            while abs(nums[i + distance] - nums[i]) > t and distance:
                distance -= 1
            if abs(nums[i + distance] - nums[i]) <= t and distance != 0:
                return True
            distance = k
        return False

class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket={}
        bucket_size=t+1
        for i in range(len(nums)):
            bucket_number=nums[i]//(t+1)
            if bucket_number in bucket:
                return True
            bucket[bucket_number]=nums[i]
            if bucket_number-1 in bucket and abs(bucket[bucket_number-1]-nums[i])<=t:
                return True
            if bucket_number+1 in bucket and abs(bucket[bucket_number+1]-nums[i])<=t:
                return True
            if i>=k:
                bucket.pop(nums[i-k]//(t+1))
        return False


nums = [1,2,3,1]
k = 3
t = 0

sv = Solution()
print(sv.containsNearbyAlmostDuplicate(nums, k, t))
