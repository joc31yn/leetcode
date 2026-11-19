class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        """
        Time Complexity: O(log n)
        """
        if not self.left and not self.right:
            heapq.heappush(self.right, num)
        elif num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) > len(self.right):
                left_max = -heapq.heappop(self.left)
                heapq.heappush(self.right, left_max)
            else:
                right_min = heapq.heappop(self.right)
                heapq.heappush(self.left, -right_min)

    def findMedian(self) -> float:
        """
        Time Complexity: O(1)
        """
        if (len(self.left) + len(self.right)) % 2 == 1:
            if len(self.left) > len(self.right):
                return -self.left[0]
            return self.right[0]
        return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
