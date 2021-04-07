from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while nums1[-1] == 0 and len(nums1) > m:
            nums1.pop()
            if len(nums1) == 0:
                break

        if m == 0:
            nums1.extend(nums2)
            return
        if n == 0:
            return

        index = 0
        for num in nums2:
            while index < m:
                if nums1[index] >= num:
                    nums1.insert(index, num)
                    m += 1
                    break
                index += 1
            if index == m:
                nums1.append(num)
                continue



nums1 = [-1,-1,0,0]
m = 3
nums2 = [1]
n = 1
sv = Solution()
sv.merge(nums1, m, nums2, n)
print(nums1)
