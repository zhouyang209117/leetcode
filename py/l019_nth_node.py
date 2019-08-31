# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cnt = 0
        add_head = ListNode(0)
        add_head.next = head
        tmp = head
        while tmp:
            tmp = tmp.next
            cnt += 1
        move = cnt - n
        tmp = add_head
        while move > 0:
            tmp = tmp.next
            move -= 1
        tmp.next = tmp.next.next
        return add_head.next


if __name__ == '__main__':
    s = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    result = s.removeNthFromEnd(node, 5)
    while result is not None:
        print(result.val)
        result = result.next
