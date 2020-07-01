# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def initList(self, nums):
        head = ListNode(nums[0])
        p = head
        for i in nums[1:]:
            p.next = ListNode(i)
            p = p.next
        return head

    def printList(self, node):
        items = []
        while node:
            items.append(node.val)
            node = node.next

        return items

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        p1 = self.initList(l1)
        p2 = self.initList(l2)

        # p1 = l1
        # p2 = l2

        head = ListNode(0)
        p = head

        while True:
            if not p1:
                p.next = p2
                break

            if not p2:
                p.next = p1
                break

            # print p1.val, p2.val
            if p1.val <= p2.val:
                p.next = p1
                p = p.next
                p1 = p1.next
            else:
                p.next = p2
                p = p.next
                p2 = p2.next

        # return head.next
        return self.printList(head.next)


if __name__ == '__main__':
    print Solution().mergeTwoLists([], [1, 3, 4, 5, 6])
