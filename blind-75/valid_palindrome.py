class Solution(object):
    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Time Complexity: O(n)
        """
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


sol = Solution()
print(sol.is_palindrome("rac;;12321car"))
