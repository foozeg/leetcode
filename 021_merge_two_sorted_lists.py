#21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        output = None
        last = None
        
        while l1 and l2:
            if l1.val <= l2.val:
                if output == None:
                    output, last = l1, l1
                else:
                    last.next = l1
                    last = last.next
                l1 = l1.next
            else:
                if output == None:
                    output, last = l2, l2
                else:
                    last.next = l2
                    last = last.next
                l2 = l2.next
        
        while l1:
            if output == None:
                output, last = l1, l1
            else:
                last.next = l1
                last = last.next
            l1 = l1.next
            
        while l2:
            if output == None:
                output, last = l2, l2
            else:
                last.next = l2
                last = last.next
            l2 = l2.next
        
        return output
            
#Results:
#Runtime: 55 ms, faster than 13.78% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 14 MB, less than 99.54% of Python3 online submissions for Merge Two Sorted Lists.
