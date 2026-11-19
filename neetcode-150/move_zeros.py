from typing import List


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         Time Complexity: O(n^2)
#         - works but slow
#         """
#         num_zeros = 0
#         for i in range(len(nums) - 1, -1, -1):
#             if nums[i] == 0:
#                 for j in range(i, len(nums) - num_zeros - 1):
#                     temp = nums[j]
#                     nums[j] = nums[j + 1]
#                     nums[j + 1] = temp
#                 num_zeros += 1
#         return nums


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Time Complexity: O(n)
        """
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[non_zero]
                nums[non_zero] = temp
                non_zero += 1
        return nums
