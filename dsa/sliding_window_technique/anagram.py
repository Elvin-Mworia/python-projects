class Solution:
    def anagram(self,s:str,p:str)->list[int]:
        if len(p)>len(s): return []
        sCount,pCount={},{}
        

        for i in range(len(p)):
            pCount[p[i]]=1+pCount.get(p[i],0)
            sCount[s[i]]=1+sCount.get(s[i],0)
            print(f'{sCount}{" "}{pCount}')

        res=[0] if sCount==pCount else []
        l=0
        for r in range(len(p),len(s)):
            sCount[s[r]]=1+sCount.get(s[r],0)
            sCount[s[l]]-=1
            print(f'{sCount}{" "}{pCount}')
            if sCount[s[l]]==0:
                sCount.pop(s[l])
        
            l+=1
            if sCount==pCount:
                res.append(l)
        print(res)
        return res
problem=Solution()

print(problem.anagram("cbajdjdbacee","abc"))




        

        

        