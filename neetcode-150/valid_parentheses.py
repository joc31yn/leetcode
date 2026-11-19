class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Time Complexity: O(n)
        """
        if len(s) < 2:
            return False
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        for letter in s:
            if letter in pairs:
                stack.append(letter)
            elif len(stack) > 0:
                # find closing pair
                top = stack.pop()
                # wrong pair matching
                if pairs[top] != letter:
                    return False
            # closing with no opening pair
            else:
                return False
        # check if all opening pairs have been closed
        return False if len(stack) > 0 else True
