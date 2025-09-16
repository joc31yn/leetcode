# class Solution(object):
#     """
#     Using .append instead of predefining res = [1] * length is reason
#     for slow time on LeetCode (I think)
#     """

#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         Time Complexity: O(3n) => O(n)
#         Space: O(n)
#         """
#         length = len(nums)
#         right = [1] * length
#         right[length - 1] = nums[length - 1]
#         for i in range(1, length):
#             right[length - i - 1] = nums[length - i - 1] * right[length - i]
#         for i in range(1, length):
#             nums[i] *= nums[i - 1]
#         res = []
#         for i in range(length):
#             if i == 0:
#                 res.append(right[1])
#             elif i == length - 1:
#                 res.append(nums[length - 2])
#             else:
#                 res.append(nums[i - 1] * right[i + 1])
#         return res


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Time Complexity: O(2n) => O(n)
        Space: O(1) excluding output
        """
        length = len(nums)
        res = [1] * length

        # store prefixes
        for i in range(1, length):
            res[i] = res[i - 1] * nums[i - 1]
        suffix_prod = 1
        # multiply suffix where necessary
        for i in range(length - 2, -1, -1):
            suffix_prod *= nums[i + 1]
            res[i] *= suffix_prod
        return res
