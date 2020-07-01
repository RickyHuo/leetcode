# encoding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head = self.initList(head)
        p = head
        reverse_p = ListNode(0)

        while p:
            if reverse_p.next:
                tmp = p
                next_node = p.next
                node = reverse_p.next
                tmp.next = node
                reverse_p.next = tmp
                p = next_node

            else:
                node = ListNode(p.val)
                reverse_p.next = node
                p = p.next

        return self.printList(reverse_p.next)

    def reverseList_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # head = self.initList(head)
        p = head
        reverse_p = ListNode(0)

        while p:
            tmp = p
            next_node = p.next
            node = reverse_p.next
            tmp.next = node
            reverse_p.next = tmp
            p = next_node

        return reverse_p.next

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


if __name__ == '__main__':
    print Solution().reverseList([1, 2, 3, 4, 5])
    # 优化版本
    print Solution().reverseList_1([1, 2, 3, 4, 5])