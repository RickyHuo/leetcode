# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        headP = ListNode(None)
        tailP = ListNode(None)
        # 新的List
        p = tailP
        q = head
        pre = headP
        h = pre
        while q:
            if q.val >= x:
                p.next = q
                p = p.next
                pre.next = q.next
            else:
                pre.next = q
                pre = q
            q = q.next
        p.next = None

        pre.next = tailP.next

        return h.next


if __name__ == "__main__":
    p = ListNode(None)
    head = p
    for i in [1, 4, 3, 2, 5, 2]:
        p.next = ListNode(i)
        p = p.next
    s = Solution().partition(head.next, 3)

    # for i in [1, 2, 3, 4, 5, 6]:
    #     p.next = ListNode(i)
    #     p = p.next
    # s = Solution().partition(head.next, 8)
    while s:
        print(s.val)
        s = s.next
