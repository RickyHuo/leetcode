# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        p = head
        while p:
            count += 1
            p = p.next

        p = head
        c = 0
        while p:
            if c == count // 2:
                return p
            count += 1
            p = p.next

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