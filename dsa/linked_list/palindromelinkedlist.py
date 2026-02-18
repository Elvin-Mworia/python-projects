class node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution(node):
    def isPallindrome(self,head:node)->bool:
        fast,slow=head,head

        while fast and fast.next: #finding middle(slow)
            fast=fast.next
            fast=fast.next
            slow=slow.next

        prev=None
        while slow.next: #reversing the second half
            tmp=slow.next
            slow.next=prev
            prev=slow
            slow=tmp
        
        left,right=head,prev

        while right:
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True



