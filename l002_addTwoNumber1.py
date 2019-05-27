# coding: utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def get_carry_value(self, val_sum):
        if val_sum >= 10:
            carry = 1
            val = val_sum - 10
        else:
            carry = 0
            val = val_sum
        return carry, val

    def last_node(self, head, tail, carry):
        if carry == 0:
            return head.next
        else:
            current = ListNode(1)
            tail.next = current
            return head.next

    def restNode(self, l, head, tail, carry):
        while l is not None:
            val_sum = carry + l.val
            carry, val = self.get_carry_value(val_sum)
            current = ListNode(val)
            tail.next = current
            tail = current
            l = l.next
        return self.last_node(head, tail, carry)

    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = tail = ListNode(0)
        while (l1 is not None) and (l2 is not None):
            val_sum = l1.val + l2.val + carry
            carry, val = self.get_carry_value(val_sum)
            current = ListNode(val)
            tail.next = current
            tail = current
            l1 = l1.next
            l2 = l2.next
        if l1 is None and l2 is None:
            return self.last_node(head, tail, carry)
        if l1 is None:
            return self.restNode(l2, head, tail, carry)
        if l2 is None:
            return self.restNode(l1, head, tail, carry)


def convertList(data):
    pre = None
    head = None
    for d in data:
        current = ListNode(d)
        if pre is not None:
            pre.next = current
            pre = current
        else:
            pre = current
            head = pre
    return head


def print_list(l):
    while l is not None:
        print(l.val)
        l = l.next


if __name__ == '__main__':
    l1 = [0]
    l2 = [1]
    v1 = convertList(l1)
    v2 = convertList(l2)
    s = Solution()
    print_list(s.addTwoNumbers(v1, v2))