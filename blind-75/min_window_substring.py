# class Solution(object):
#     def t_in_s(self, freq_s, freq_t):
#         for key, value in freq_t.items():
#             if key not in freq_s or freq_s[key] < value:
#                 return False
#         return True
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         Time Complexity: O(n^2) :(
#          - looping through each key value pair in dict everytime a
#            valid letter is added which is inefficient
#         """
#         freq_t = {}
#         for letter in t:
#             freq_t[letter] = 1 + freq_t.get(letter, 0)
#         freq_s = {}
#         start, end = 0, 0
#         min_sub = ""
#         moving_start = False
#         while start < len(s) and end < len(s):
#             if s[start] not in freq_t:
#                 if s[start] in freq_s:
#                     freq_s[s[start]] -= 1
#                 start += 1
#                 if start > end:
#                     end = start
#                 continue
#             freq_s[s[end]] = 1 + freq_s.get(s[end], 0)
#             if moving_start:
#                 freq_s[s[end]] -= 1
#                 moving_start = False
#             if s[end] in freq_t and self.t_in_s(freq_s, freq_t):
#                 substring = s[start: end + 1]
#                 if min_sub == "" or len(min_sub) > end - start + 1:
#                     min_sub = substring
#                 moving_start = True
#                 freq_s[s[start]] -= 1
#                 start += 1
#             else:
#                 end += 1
#         return min_sub


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        Better sol - still not too good
        """
        freq_t = {}
        for letter in t:
            freq_t[letter] = 1 + freq_t.get(letter, 0)
        need = len(freq_t)
        have = 0
        min_sub = ""
        freq_s = {}
        start, end = 0, 0
        same_end = False
        while start < len(s) and end < len(s):
            if s[start] not in freq_t:
                start += 1
                if start > end:
                    end = start
                continue

            if s[end] in freq_t:
                freq_s[s[end]] = 1 + freq_s.get(s[end], 0)
                if same_end:
                    freq_s[s[end]] -= 1
                if freq_s[s[end]] == freq_t[s[end]] and not same_end:
                    have += 1
                if have == need:
                    if min_sub == "" or len(min_sub) > end - start + 1:
                        min_sub = s[start: end + 1]
                    freq_s[s[start]] -= 1
                    if freq_s[s[start]] < freq_t[s[start]]:
                        have -= 1
                    start += 1
                    same_end = True
                else:
                    same_end = False
                    end += 1
            else:
                same_end = False
                end += 1
        return min_sub
