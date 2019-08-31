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

    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = tail = ListNode(0)
        while l1 or l2 or carry != 0:
            val_sum = 0
            if l1 is not None:
                val_sum += l1.val
                l1 = l1.next
            if l2 is not None:
                val_sum += l2.val
                l2 = l2.next
            val_sum += carry
            carry, val = self.get_carry_value(val_sum)
            current = ListNode(val)
            tail.next = current
            tail = current
        return head.next


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
    l1 = [9]
    l2 = [1, 9, 9]
    v1 = convertList(l1)
    v2 = convertList(l2)
    s = Solution()
    print_list(s.addTwoNumbers(v1, v2))