class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity: O(log n)
         - binary search
        """
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[0]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid
            # could just be else because not possible for both conditions to be true
            elif nums[mid] < nums[l]:
                r = mid
            if r - l == 1:
                return nums[r]
        return nums[l]
