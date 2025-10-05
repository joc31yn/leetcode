# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) < 2:
#             return len(s)
#         longest = 1
#         current = 1
#         seen = {s[0] : 0}
#         i = 1
#         while i < len(s):
#             if s[i] not in seen:
#                 current += 1
#                 seen[s[i]] = i
#                 i += 1
#             else:
#                 longest = max(longest, current)
#                 current = 0
#                 i = seen[s[i]] + 1
#                 seen = {}
#                 if len(s) - longest <= i:
#                     break
#         longest = max(longest, current)
#         return longest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Time Complexity: O(n)
          - Sliding window
        """
        if len(s) < 2:
            return len(s)
        start, end = 0, 1
        seen = set(s[0])
        longest = 1
        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
            else:
                longest = max(longest, end - start)
                while s[start] != s[end]:
                    seen.remove(s[start])
                    start += 1
                start += 1
                end += 1
        longest = max(longest, end - start)
        return longest
