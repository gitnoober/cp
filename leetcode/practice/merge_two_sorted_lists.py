# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        res = dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1, res = list1.next, res.next

            else:
                res.next = list2
                list1, res = list2.next, res.next

        if list1 or list2:
            res.next = list1 if list1 else list2

        return dummy.next


def swappairs(head):

    # 1, 2, 3, 4
    # 2, 1, 4, 3
    pass
