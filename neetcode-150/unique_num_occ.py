class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        Time Complexity: O(n)
        """
        freq = {}
        for n in arr:
            freq[n] = 1 + freq.get(n, 0)
        seen = set()
        for val in freq.values():
            if val not in seen:
                seen.add(val)
            else:
                return False
        return True
