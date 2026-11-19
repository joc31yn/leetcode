# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         """
#         Slow
#         """
#         head = ListNode()
#         temp = head
#         while True:
#             min_index = -1
#             for i in range(len(lists)):
#                 if lists[i] and (min_index < 0 or lists[i].val < lists[min_index].val):
#                     min_index = i
#             if min_index == -1:
#                 break
#             head.next = lists[min_index]
#             lists[min_index] = lists[min_index].next
#             head = head.next
#         return temp.next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Time Complexity: O(n * log(k))
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(list1, list2))
            lists = merged_lists
        return lists[0]
