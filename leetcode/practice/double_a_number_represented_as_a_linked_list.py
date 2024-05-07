from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_ll(self, node):
        prev, curr = None, node
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = self.reverse_ll(head)
        p = prev
        pp = p
        while p:
            t = p.val * 2
            tot = t + carry
            if t <= 9:
                p.val = tot
                carry = 0
            else:
                p.val = tot % 10
                carry = t // 10
            pp = p
            p = p.next
        if carry:
            pp.next = ListNode(carry)
        return self.reverse_ll(prev)

        # 1 8 9 --> 9 8 1
        # 8 7 3
