class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)+1
        m=len(nums2)+1
        dp=[]
        for _ in range(n):
            dp.append([0]*m)
        for i in range(1,n):
            for j in range(1,m):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
        maxx=0
        for i in range(n):
            maxx=max(maxx,max(dp[i]))
        return maxx