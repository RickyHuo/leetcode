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
        head = self.initList(head)
        p = head

        reverse_p = ListNode(0)
        # reverse_head = reverse_p
        import time
        while p:
            print p.val
            if reverse_p.next:
                b_node = reverse_p.next
                node = ListNode(p.val)
                reverse_p.next = node
                node.next = b_node

            else:
                node = ListNode(p.val)
                reverse_p.next = node

            # print self.printList(reverse_p)
            p = p.next

        return reverse_p.next
        # return self.printList(reverse_p.next)

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
    print Solution().reverseList([1])