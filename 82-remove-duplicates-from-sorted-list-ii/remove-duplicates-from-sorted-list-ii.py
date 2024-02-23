# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check if value of current is same as last value. need 2 ptrs
        
        dummy = ListNode(0,head)
        p1 = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                p1.next = curr.next

            else:
                p1 = p1.next
            curr = curr.next

        return dummy.next

        