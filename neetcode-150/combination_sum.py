class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity: O(2^(t/m)), t = target
        """
        sol = []

        def backtrack(i: int, cur_vals: List[int], cur_sum: int):
            if cur_sum == target:
                sol.append(cur_vals.copy())
                return
            if i >= len(candidates) or cur_sum > target:
                return
            # include candidates[i]
            cur_vals.append(candidates[i])
            backtrack(i, cur_vals, cur_sum + candidates[i])
            # skip candidates[i]
            cur_vals.pop()
            backtrack(i + 1, cur_vals, cur_sum)

        backtrack(0, [], 0)
        return sol
