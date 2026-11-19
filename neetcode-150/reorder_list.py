# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        Time Complexity: O(n)
        Space: O(1)
        - key is finding where to split and reversing second half
        - then easily merge
        """
        # determine where middle of ll is
        slow, fast = head, head
        while fast and fast.next:
            if fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                fast = fast.next
        rev_list = None
        curr = slow.next  # begin reversing list after first half end
        slow.next = None  # then terminate first half list
        while curr:
            temp = curr.next
            curr.next = rev_list
            rev_list = curr
            curr = temp
        # merge lists, can assume start list >= tail in length from above logic
        start = head
        tail = fast
        while start:
            start_temp = start.next
            tail_temp = tail.next
            start.next = tail
            tail.next = start_temp
            start = start_temp
            tail = tail_temp
            if not tail:
                break
