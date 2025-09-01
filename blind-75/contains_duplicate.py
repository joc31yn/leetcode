from typing import List


def has_duplicate(nums: List[int]) -> bool:
    seen = []
    for num in nums:
        if num in seen:
            return True
        seen.append(num)
    return False


print(has_duplicate([1, 2, 3]))
