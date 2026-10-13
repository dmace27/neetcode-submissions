# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        ptr = l1
        lastOver10 = False
        while ptr != None:
            ptr = ptr.next
            n += 1
        
        dummy1 = ListNode()
        d1 = dummy1
        p1 = l1
        p2 = l2
        for i in range(n):
            add = p1.val + p2.val
            p1 = p1.next
            p2 = p2.next
            if lastOver10:
                lastOver10 = False
                add += 1
            
            # create node for 
            b = ListNode()
            b.val = add
            if add > 9:
                b.val -= 10
                lastOver10 = True            
            # move the pointer along
            d1.next = b
            d1 = d1.next
        
        if lastOver10:
            a = ListNode()
            a.val = 1
            d1.next = a
        
        return dummy1.next
            
