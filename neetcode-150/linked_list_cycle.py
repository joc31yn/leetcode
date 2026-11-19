# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Time Complexity: O(n)
        Space: O(n)
        """
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)
            curr = curr.next
        return False


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         Time Complexity: O(n)
#         Space: O(1)
#         - Floyd's tortoise and hare cycle-finding algorithm
#         - idea is the if there is a cycle, 'hare' (fast pointer) will
#         eventually catch up to 'tortoise' (slow pointer)
#         """
#         turtle, hare = head, head
#         while hare and hare.next:
#             turtle = turtle.next
#             hare = hare.next.next
#             if turtle == hare:
#                 return True
#         return False
