# class Solution(object):
#     def top_k_frequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         works but very slow
#         """
#         frequencies = {}
#         for num in nums:
#             if num in frequencies:
#                 frequencies[num] += 1
#             else:
#                 frequencies[num] = 1
#         maxes = []
#         for i in range(k):
#             max = float('-inf')
#             max_key = None
#             for key, val in frequencies.items():
#                 if val > max:
#                     max = val
#                     max_key = key
#             maxes.append(max_key)
#             frequencies[max_key] = float('-inf')
#         return maxes


class Solution2(object):
    def top_k_frequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        Bucket Sort Approach
        """
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        maxes = [None]*len(nums)

        for key, val in frequencies.items():
            if maxes[val - 1] is None:
                maxes[val - 1] = [key]
            else:
                maxes[val - 1].append(key)
        sol = []
        for arr in maxes[::-1]:
            if not (arr is None):
                length = len(arr)
                if k == length:
                    sol.extend(arr)
                    break
                elif k < length:
                    sol.extend(arr[:k])
                    break
                else:
                    sol.extend(arr)
                    k -= length
        return sol


sol = Solution2()
print(sol.top_k_frequent([1, 1, 3, 2, 2, 2], 2))
