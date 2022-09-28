class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        li=[arr[0]]
        ans=[]
        for i in range(1,len(arr)):
            li.append(li[-1]^arr[i])
        for left,right in queries:
            if left==0:
                ans.append(li[right])
            else:
                ans.append(li[left-1]^li[right])
        return ans
            
        