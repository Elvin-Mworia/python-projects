class Solution():
    def minimumSub(self,t:int,arr:list[int])->int:
        l,total=0,0
        res=float("inf")

        for r in range(len(arr)):
            total+=arr[r]
            while total>=t:
                res=min((r-l+1),res)
                total-=arr[l]
                l+=1

        return 0 if res==float("inf") else res # type: ignore
    
problem=Solution()
print(problem.minimumSub(8,[1,1,1,1,2,3,4]))