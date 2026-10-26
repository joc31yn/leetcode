class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time: O(n)
        """
        if not s:
            return False

        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        """
        Time: O(2^n)
         - total of n - 1 gaps to split and for each one you can choose
           to split or not split
        """
        sol = []
        curr = []
        
        def recurse(start: int) -> None:
            # at end of substr, so add copy of substr partitions
            if start >= len(s):
                sol.append(curr.copy())
                return

            # backtrack on smaller substr
            for i in range(start, len(s)):
                first = s[start:i + 1]
                if self.isPalindrome(first):
                    curr.append(first)  # current choice
                    recurse(i + 1)  # explore deeper
                    curr.pop()  # backtrack
        recurse(0)
        return sol
