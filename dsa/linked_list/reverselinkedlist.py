class node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def reverseList(self,head:node)->node:
            prev,curr=None,head

            while curr:
                 nxt=curr.next
                 curr.next=prev
                 prev=curr
                 curr=nxt
            return prev # type: ignore



