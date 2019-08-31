# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_list_len(head):
    cnt = 0
    tmp = head
    while tmp:
        cnt += 1
        tmp = tmp.next
    return cnt


def forword(head, k):
    tmp = head
    add_head = ListNode(0)
    for i in range(k):
        p = tmp.next
        cache = add_head.next
        add_head.next = tmp
        tmp.next = cache
        tmp = p
    return add_head.next, tmp


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        list_len = get_list_len(head)
        part = list_len // k
        add_head = ListNode(0)
        add_head.next = None
        tmp_end = add_head
        tmp_head = head
        next = head
        for i in range(part):
            tmp_result, next = forword(tmp_head, k)
            tmp_head = next
            tmp_end.next = tmp_result
            for j in range(k):
                tmp_end = tmp_end.next
        tmp_end.next = next
        return add_head.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    s = Solution()
    result = s.reverseKGroup(None, 1)
    while result:
        print(result.val)
        result = result.next

