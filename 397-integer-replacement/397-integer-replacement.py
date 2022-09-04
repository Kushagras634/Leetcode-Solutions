class Solution:
    def integerReplacement(self, n: int) -> int:
        def inte(n,dp):
            if n==1:
                return 0
            if n in dp:
                return dp[n]
            if n%2==0:
                dp[n]=1+inte(n//2,dp)
            if n%2!=0:
                dp[n]=1+min(inte(n+1,dp),inte(n-1,dp))
            return dp[n]
        dp={}
        return inte(n,dp)
                
        