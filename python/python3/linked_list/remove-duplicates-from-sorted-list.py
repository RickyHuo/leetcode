# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
        return head