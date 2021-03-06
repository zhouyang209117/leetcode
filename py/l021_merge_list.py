# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        add_head = ListNode(0)
        last = add_head
        while l1 and l2:
            if l1.val < l2.val:
                last.next = l1
                l1 = l1.next
            else:
                last.next = l2
                l2 = l2.next
            last = last.next
        while l1:
            last.next = l1
            l1 = l1.next
            last = last.next
        while l2:
            last.next = l2
            l2 = l2.next
            last = last.next
        return add_head.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    node2 = ListNode(-1)
    node2.next = ListNode(3)
    node2.next.next = ListNode(4)
    node2.next.next.next = ListNode(8)
    node2.next.next.next.next = ListNode(9)
    s = Solution()
    result = s.mergeTwoLists(node1, node2)
    while result is not None:
        print(result.val)
        result = result.next