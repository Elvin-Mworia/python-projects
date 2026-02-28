class node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def isPallindrome(self,head:node)->bool:
        nums=[]

        while head:
            nums.append(head.val)
            head=head.next # type: ignore
        
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]!=nums[r]:
                return False
            l+=1
            r-=1
        return True

    