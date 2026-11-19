# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         Time Complexity: O(2 log n) => O(log n) - relatively slow
#         """
#         # find pivot point
#         l, r = 0, len(nums) - 1
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] > nums[r]:
#                 l = mid + 1
#             else:
#                 r = mid
#         # first index of right side
#         pivot = r
#         search_left = True
#         if target >= nums[pivot] and target <= nums[len(nums) - 1]:
#             search_left = False
#         l_1 = 0 if search_left else pivot
#         r_1 = pivot - 1 if search_left else len(nums) - 1
#         while l_1 <= r_1:
#             mid = (l_1 + r_1) // 2
#             if target == nums[mid]:
#                 return mid
#             elif target > nums[mid]:
#                 l_1 = mid + 1
#             else:
#                 r_1 = mid - 1
#         return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > nums[r]:
                # check left side
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            # check right side
            elif target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
