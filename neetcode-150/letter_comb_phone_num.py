class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Time Complexity: O(4^n) where n is the length of `digits`

        alt sol has better space complexity
        """
        letter_to_number = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }

        # # needed only if restriction for digits allows "" (empty string)
        # if not digits:
        #     return []

        # bottom-up construction
        def backtrack(digits: str) -> list[str]:
            if len(digits) == 1:
                return letter_to_number[digits]
            combs = backtrack(digits[1:])
            curr_digit = digits[0]
            new = []
            for l in letter_to_number[curr_digit]:
                for c in combs:
                    new.append(l + c)
            return new
        return backtrack(digits)

        # # alt sol, build top-down
        # def backtrack2(i: int, curr_str: str) -> list[str]:
        #     if len(curr_str) == len(digits):
        #         sol.append(curr_str)
        #         return
        #     for c in letter_to_number[digits[i]]:
        #         backtrack2(i + 1, curr_str + c)
        # if digits:
        #   backtrack2(0, "")
        
