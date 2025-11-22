# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        temp = head
        count = 0
        # find length of linked list
        while temp:
            temp = temp.next
            count += 1
        if count - n == 0:
            return head.next
        start = head
        prev = start
        # remove length - nth node from front
        while count - n > 0:
            count -= 1
            prev = start
            start = start.next
        prev.next = start.next
        start.next = None
        return head
