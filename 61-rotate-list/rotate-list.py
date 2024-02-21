# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        last = head
        length = 1

        while last.next:
            last = last.next
            length += 1
        
        last.next = head

        for i in range(length - k % length):
            last = last.next

        dummy = last.next
        last.next = None

        return dummy 
