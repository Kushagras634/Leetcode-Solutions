class Solution:
    def rob(self, nums: List[int]) -> int:
        inclusive=nums[0]
        exclusive=0
        n=len(nums)
        for i in range(1,n):
            x=inclusive
            inclusive=exclusive+nums[i]
            exclusive=max(x,exclusive)
        return max(inclusive,exclusive)
        