# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        only move p1 after a re-linking
        instead of a swap, do a rewire where nexts are overwritten
        '''

        batch1 = ListNode(0)
        p1 = batch1
        batch2 = ListNode(0)
        p2 = batch2

        curr = head

        while curr:
            if curr.val < x:
                p1.next = curr
                p1 = p1.next

            else:
                p2.next = curr
                p2 = p2.next

            curr = curr.next

        p1.next = batch2.next
        p2.next = None

        return batch1.next