class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        else:
            for i in range(2,n):
                if i==2:
                    x=nums[i-2]
                    nums[i]+=x
                else:
                    x=max(nums[i-2],nums[i-3])
                    nums[i]+=x
        return max(nums[n-1],nums[n-2])
        