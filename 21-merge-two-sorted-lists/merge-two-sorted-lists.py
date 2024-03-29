# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        plan :
        1 ptr on null head. stays so it can be returned. 
        1 ptr on 1st list to move and compare.
        1 ptr on 2nd list to move and compare.
        
        if item at ptr is less, then that is next and then next moves
        
        '''
        curr = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            
        curr.next = list1 or list2
        return head.next
