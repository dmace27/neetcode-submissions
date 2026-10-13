# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        count = 0
        while fast.next:
            slow = slow.next
            fast = fast.next
            count += 1
            if fast.next:
                fast = fast.next
                count += 1
        
        # edge cases:

        # if list length is 2:
        if count > 2:
            middle = slow
            p1 = middle
            p2 = middle.next
            middle.next = None

            while p2: 
                temp = p2.next
                p2.next = p1
                p1 = p2
                p2 = temp

            head1 = head
            head2 = p1
            next2 = head2.next
            next1 = head.next

            while next1:
                head1.next = head2
                head2.next = next1
                head1 = next1
                next1 = next1.next
                head2 = next2
                if next2.next:
                    next2 = next2.next
                else:
                    break





            