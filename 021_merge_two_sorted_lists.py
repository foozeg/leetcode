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
                output, last, l1 = self.process(output, last, l1)
            else:
                output, last, l2 = self.process(output, last, l2)
        
        while l1:
            output, last, l1 = self.process(output, last, l1)
            
        while l2:
            output, last, l2 = self.process(output, last, l2)
        
        return output
        
    def process(self, output, last, link_list):
        if output == None:
            output, last = link_list, link_list
        else:
            last.next = link_list
            last = last.next
        
        return output, last, link_list.next
  
#Results:
#Runtime: 32 ms, faster than 92.46% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 14.4 MB, less than 30.86% of Python3 online submissions for Merge Two Sorted Lists.
