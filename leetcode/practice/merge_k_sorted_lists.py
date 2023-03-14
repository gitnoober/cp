# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_2_lists(aa, bb):
            point = ListNode(0)
            p = point
            a = aa
            b = bb
            while a is not None and b is not None:
                if a.val > b.val:
                    point.next = ListNode(b.val)
                    b = b.next
                else:
                    point.next = ListNode(a.val)
                    a = a.next
                point = point.next
            while a is not None:
                point.next = ListNode(a.val)
                a = a.next
                point = point.next
            while b is not None:
                point.next = ListNode(b.val)
                b = b.next
                point = point.next
            return p.next

        tot_len = len(lists)
        interval = 1
        while interval < tot_len:
            for i in range(0, tot_len - interval, interval * 2):
                x = merge_2_lists(lists[i], lists[i + interval])
                lists[i] = x
            interval *= 2

        return lists[0] if lists else None
