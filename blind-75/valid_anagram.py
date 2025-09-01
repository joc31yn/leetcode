class Solution:
    def generate_dict(self, s: str) -> dict:
        chars = {}
        for letter in s:
            if letter in chars:
                chars[letter] += 1
            else:
                chars[letter] = 1
        return chars

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n + m), n and m and length of s and t respectively
        """
        if len(s) != len(t):
            return False
        # alternataively bc they are same length no need for helper function
        # only one loop is necessary to add key value paris
        char_s = self.generate_dict(s)
        char_t = self.generate_dict(t)
        if char_s == char_t:
            return True
        return False


sol = Solution()

# Test cases
print(sol.isAnagram("listen", "silent"))  # True
print(sol.isAnagram("hello", "bello"))  # False
