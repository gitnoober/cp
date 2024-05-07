from typing import List, Optional


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

	def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    	prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        dummy_node = ListNode(-1)
        temp_prev, curr = dummy_node, prev
        while curr:
            if curr.val >= temp_prev.val:
                temp_prev.next = curr
                temp_prev = temp_prev.next
            curr = curr.next
        temp_prev.next = None
        self.reverse_ll(dummy_node.next)

        # prev, curr = None, dummy_node.next
        # while curr:
        #     curr.next, prev, curr = prev, curr, curr.next
        # return prev
