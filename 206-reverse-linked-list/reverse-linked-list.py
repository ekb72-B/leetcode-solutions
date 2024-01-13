# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr,nnext = None,head,None
        
        while curr is not None:
            nnext = curr.next
            curr.next = prev
            prev = curr
            curr = nnext
            
        return prev