class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Time Complexity: O(n)
        - trick for storing max_freq, dont need to decrement it
        when shifting window left since only care about max length
        """
        if len(s) < 2:
            return len(s)
        start, end = 0, 1
        freq = {s[0]: 1}
        longest = 1
        max_freq = 1
        while end < len(s):
            if s[end] not in freq:
                freq[s[end]] = 1
            else:
                freq[s[end]] += 1
                max_freq = max(max_freq, freq[s[end]])
            window_len = end - start + 1
            replacements = window_len - max_freq
            if replacements > k:
                longest = max(longest, window_len - 1)
                while replacements > k:
                    freq[s[start]] -= 1
                    start += 1
                    window_len = end - start + 1
                    replacements = window_len - max_freq
            end += 1
        longest = max(longest, end - start)
        return longest


class SolutionSimplified(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Time Complexity: O(n)
        - better/simpler python syntax i guess :D
        """
        if len(s) < 2:
            return len(s)
        start, end = 0, 1
        freq = {s[0]: 1}
        longest = 1
        max_freq = 1
        while end < len(s):
            freq[s[end]] = 1 + freq.get(s[end], 0)
            max_freq = max(max_freq, freq[s[end]])
            while end - start + 1 - max_freq > k:
                freq[s[start]] -= 1
                start += 1
            end += 1
            longest = max(longest, end - start)
        return longest
