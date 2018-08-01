# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        head = self.initList(head)

        if m == n:
            return head
        p = head
        reverse = ListNode(0)
        head = reverse
        flag = 0
        count = 1

        while p:
            if m <= count <= n:
                if flag == 0:
                    first_node = p
                    flag = 1
                else:
                    pass

                tmp = p
                next_node = p.next
                node = reverse.next
                tmp.next = node
                reverse.next = tmp
                p = next_node

            else:
                if flag == 0:
                    reverse.next = p
                    reverse = reverse.next
                else:
                    first_node.next = p
                    return self.printList(head.next)
                p = p.next

            count += 1

        first_node.next = None
        return self.printList(head.next)

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
    print Solution().reverseBetween([1, 2, 3, 4, 5], 2, 4)