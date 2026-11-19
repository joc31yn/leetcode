# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         seen_triplets = set()
#         if len(nums) < 3:
#             return res
#         nums = sorted(nums)
#         for i in range(len(nums) - 2):
#             s = i + 1
#             e = len(nums) - 1
#             target = -nums[i]
#             while s < e:
#                 start = nums[s]
#                 end = nums[e]
#                 if start + end == target:
#                     triplet = [nums[i], start, end]
#                     if tuple(triplet) not in seen_triplets:
#                         res.append(triplet)
#                     seen_triplets.add(tuple(triplet))
#                     s += 1
#                     e -= 1
#                 elif start + end < target:
#                     s += 1
#                 else:
#                     e -= 1
#         return res


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Time Complexity: O(n^2)
          - key is sorting array first
          - instead of checking entire duplicate triplets as tuples,
            only need to check repeated starting vals and duplicate pairs
        """
        res = []
        if len(nums) < 3:
            return res
        nums = sorted(nums)
        seen_starts = set()
        for i in range(len(nums) - 2):
            if nums[i] not in seen_starts:
                seen_starts.add(nums[i])
                s = i + 1
                e = len(nums) - 1
                target = -nums[i]
                while s < e:
                    start = nums[s]
                    end = nums[e]
                    if start + end == target:
                        res.append([nums[i], start, end])
                        # move pointers to next unique val to avoid repition
                        while s + 1 < len(nums) and nums[s] == nums[s + 1]:
                            s += 1
                        while e - 1 >= 0 and nums[e] == nums[e - 1]:
                            e -= 1
                        # if no repition, move 1 inward
                        s += 1
                        e -= 1
                    elif start + end < target:
                        s += 1
                    else:
                        e -= 1
        return res


sol = Solution()
print(sol.threeSum([0, 2, 1, -1, 5, 6]))
