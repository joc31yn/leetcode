from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n)
        """
        seen = {}
        length = len(nums)
        for i in range(length):
            val = target - nums[i]
            if val in seen:
                return [seen[val], i]
            seen[nums[i]] = i
        return []


sol = Solution()

print(sol.two_sum([1, 2, 3, 4, 5], 9))
print(sol.two_sum([3, 2, 4, 4, 7], 8))
