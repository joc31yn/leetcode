# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Time Complexity: O(n + m)
        """
        head = ListNode()
        temp = head
        while list1 or list2:
            if not list1:
                head.next = list2
                break
            elif not list2:
                head.next = list1
                break
            elif list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        return temp.next


# class SolutionRecursive:
#     def mergeTwoLists(
#         self, list1: Optional[ListNode], list2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         if list1.val < list2.val:
#             return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
#         return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
