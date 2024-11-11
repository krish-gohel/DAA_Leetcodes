class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        l1=[True for i in range(n+1)]
        l1[0]=l1[1]=False
        for i in range(len(l1)):
            if(l1[i]):
                for j in range(i*i,len(l1),i):
                        l1[j]=False
        ans=[]
        for i1 in range(n+1):
            if(l1[i1]):
                ans.append(i1)
        n1=len(ans)
        ans=1
        for i in range(1,n1+1):
            ans*=i
        for j in range(1,n-n1+1):
            ans*=j
        return(ans%(10**9+7))