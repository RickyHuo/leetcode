# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head.next:
            return head

        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right_head = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(right_head)

        return self.merge(left, right)

    @staticmethod
    def merge(left, right):

        # val = min(left.val, right)

        p = ListNode(-1)
        head = p

        while left and right:
            if left.val < right.val:

                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
            p.next = None
        if left:
            p.next = left
        if right:
            p.next = right

        return head.next


def init_list(source):
    head = ListNode(-1)
    head_1 = head
    for i in source:
        p = ListNode(i)
        head.next = p
        head = head.next

    return head_1.next


if __name__ == '__main__':
    p = init_list([4, 5, 3, 1, 2])
    # print(p.val)
    # print(p.next.val)
    s = Solution()
    s.sortList(p)
    String
