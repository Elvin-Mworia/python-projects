class Solution:

    def topkelements(self,numarr:list[int],k:int):
        count={}
        freq=[[] for i in range(len(numarr)+1)]
        
        for n in numarr:
            count[n]=1+count.get(n,0)
        print(count)
        for n,c in count.items():
            freq[c].append(n)

        res=[]
        for n in range(len(freq)-1,0,-1):#traverse the freq list in descending order
            for i in freq[n]:
                res.append(i)
                if len(res)==k:
                    print(res)
                    return res

problem=Solution()

problem.topkelements([1,2,2,2,3,3,3,4],2)