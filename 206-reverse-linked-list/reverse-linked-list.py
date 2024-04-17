# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        if not head:
            return
        
        while curr:
            nnext = curr.next
            curr.next = prev
            prev = curr
            curr = nnext
        
        return prev
