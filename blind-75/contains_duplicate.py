from typing import List


def has_duplicate(nums: List[int]) -> bool:
    """
    Time Complexity: O(n) with hashset
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


print(has_duplicate([1, 2, 3]))
