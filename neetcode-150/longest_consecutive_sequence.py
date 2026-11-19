class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity: O(n)
        """
        nums_seen = set(nums)
        start_nums = set()
        for n in nums:
            if n - 1 not in nums_seen and n not in start_nums:
                start_nums.add(n)
        if len(start_nums) == 0:
            return 0

        start_nums = list(start_nums)
        max_len = 1
        curr_len = 1
        start_index = 0
        count = 1
        search_for = start_nums[start_index] + 1

        while count < len(nums_seen):
            if search_for in nums_seen:
                count += 1
                curr_len += 1
                search_for += 1
            else:
                max_len = max(curr_len, max_len)
                curr_len = 1
                start_index += 1
                if start_index < len(start_nums):
                    search_for = start_nums[start_index] + 1
                    count += 1
                else:
                    break
        max_len = max(curr_len, max_len)
        return max_len


# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         Intended Sol -> idk why im getting timeout on leetcode D:
#         """
#         nums_set = set(nums)
#         max_len = 0
#         for n in nums:
#             if (n - 1) not in nums_set:
#                 curr_len = 1
#                 while n + curr_len in nums_set:
#                     curr_len += 1
#                 max_len = max(max_len, curr_len)
#         return max_len
