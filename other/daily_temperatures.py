# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         for i in range(len(temperatures) - 1, -1, -1):
#             if i == len(temperatures) - 1:
#                 stack.append((temperatures[i], i))
#                 temperatures[i] = 0
#             elif temperatures[i] < stack[len(stack) - 1][0]:
#                 stack.append((temperatures[i], i))
#                 temperatures[i] = 1
#             else:
#                 while len(stack) > 0:
#                     top = stack[len(stack) - 1]
#                     if temperatures[i] < top[0]:
#                         temp = temperatures[i]
#                         temperatures[i] = top[1] - i
#                         stack.append((temp, i))
#                         break
#                     else:
#                         stack.pop()
#                 if len(stack) == 0:
#                     stack.append((temperatures[i], i))
#                     temperatures[i] = 0
#         return temperatures


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        """
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > stack[len(stack) - 1][0]:
                top = stack[len(stack) - 1]
                res[top[1]] = i - top[1]
                stack.pop()
            stack.append([temperatures[i], i])
        return res
