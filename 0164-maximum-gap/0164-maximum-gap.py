class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n=len(nums)
        mi=min(nums)
        mx=max(nums)
        averg=math.ceil((mx-mi)/(len(nums)-1))
        minB=[float('inf')]*(n-1)
        maxB=[float('-inf')]*(n-1)
        for i in range(n):
            if nums[i]==mi or nums[i]==mx:
                continue
            ind=((nums[i]-mi)*(n-1))//(mx-mi)
            minB[ind]=min(minB[ind],nums[i])
            maxB[ind]=max(maxB[ind],nums[i])
        ans=0
        for i in range(n-1):
            if minB[i]==float('inf'):
                continue
            ans=max(ans,minB[i]-mi)
            mi=maxB[i]
        ans=max(ans,mx-mi)
        return ans
            
            
            
            
            
            