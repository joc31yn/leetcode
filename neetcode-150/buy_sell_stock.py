# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         Time Complexity: O(n)
#         """
#         buy, sell = 0, 0
#         max_profit = 0
#         for i, price in enumerate(prices):
#             if price < prices[buy]:
#                 buy = i
#                 sell = i
#             if price > prices[sell]:
#                 sell = i
#             max_profit = max(max_profit, prices[sell] - prices[buy])
#         return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        Time Complexity: O(n)
          - dont need pointer for sell, save space complexity
        """
        buy = 0
        max_profit = 0
        for i, price in enumerate(prices):
            if price < prices[buy]:
                buy = i
            else:
                max_profit = max(max_profit, price - prices[buy])
        return max_profit
