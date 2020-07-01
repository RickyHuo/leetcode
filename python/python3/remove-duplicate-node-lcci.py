# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        p = head
        p_last = None
        tmp = {}
        while (True):
            try:
                tmp[p.val] += 1
                p_last.next = p.next
            except:
                tmp[p.val] = 1
                p_last = p

            if p.next == None:
                break

            p = p.next

        return head


