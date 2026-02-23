class node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def removeduplicates(self,head:Optional[node])->Optional[node]:
         curr=head

         while curr:
             while curr.next and curr.val==curr.next.val:
                 curr.next=curr.next.next
             curr=curr.next
         return head