#2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = self.addValues(l1, l2)
        return l3
        
    def addValues(self, l1, l2, pop=0):
        proceed = True
        if l1.next is None and l2.next is None:
            proceed = False
            
        val3 = l1.val + l2.val + pop
        
        if val3 >= 10:
            val3 = val3 % 10
            pop = 1
            proceed = True
        else: 
            pop = 0
            
        l3 = ListNode(val3)
        
        if l1.next is None:
            l1.next = ListNode(0) 
        if l2.next is None:
            l2.next = ListNode(0) 
        
        if proceed:
            l3.next = self.addValues(l1.next, l2.next, pop)
        
        return l3

#Results
#Runtime: 72 ms, faster than 57.11% of Python3 online submissions for Add Two Numbers.
#Memory Usage: 14.4 MB, less than 12.92% of Python3 online submissions for Add Two Numbers.

#Let's try solution without recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = True
        pop = 0
        while True:
            val3 = l1.val + l2.val + pop
            pop = int(val3/10)
            val3 = val3 % 10

            if first:
                l3 = ListNode(val3)
                first = False
                last = l3
            else:
                new = ListNode(val3)
                last.next = new
                last = new

            if l1.next is None and l2.next is None and pop == 0:
                break

            l1 = ListNode(0) if (l1.next is None) else l1.next
            l2 = ListNode(0) if (l2.next is None) else l2.next
        
        return l3
#Results
#Runtime: 72 ms, faster than 57.58% of Python3 online submissions for Add Two Numbers.
#Memory Usage: 14.2 MB, less than 90.56% of Python3 online submissions for Add Two Numbers.
