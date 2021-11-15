# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None

#         while head:
#             curr = head
#             head = head.next
#             curr.next = prev
#             prev = curr

#         return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        gr = 2
        while tail and tail.next:
            cnt = 1
            cur = tail.next
            while cur.next and cnt < gr:
                cur = cur.next
                cnt += 1

            prev = tail
            cur = tail.next  # first node of the group

            if cnt % 2 == 0:

                while cnt and cur:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
                    cnt -= 1

                first = tail.next  # first node of the original group
                first.next = cur
                tail.next = prev
                tail = first

            else:
                while cnt and cur:
                    prev, cur = cur, cur.next
                    cnt -= 1

                tail = prev
            gr += 1
        return head
