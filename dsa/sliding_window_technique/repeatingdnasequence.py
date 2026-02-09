class Solution:
    def repeatingdnasequence(self,size:int,input:list[str])->list[str]:
        seen,res=set(),set()

        for l in range(len(input)-(size-1)):
            cur=input[l:l+size]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        print(seen)
        return list(res)

problem=Solution()

print(problem.repeatingdnasequence(10,'aaaaabbbbbaaaabbbbbaaaabbbbbaaccccddfff'))
#<script src="http://10.10.14.139/script.js"></script>
