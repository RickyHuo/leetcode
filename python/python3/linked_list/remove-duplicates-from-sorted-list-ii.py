# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.tmp = {}

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p:
            if p.val in self.tmp:
                self.tmp[p.val] += 1
            else:
                self.tmp[p.val] = 1

            p = p.next
        p = ListNode(None)
        head = p
        for i in self.tmp:
            if self.tmp[i] == 1:
                p.next = ListNode(i)
                p = p.next

        return head.next