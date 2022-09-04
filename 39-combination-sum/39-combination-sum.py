class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # li=[]
        # def combination(candidates,temp,target):
        #     if sum(temp)>target:
        #         return
        #     if sum(temp)==target:
        #         li.append(temp)
        #         return
        #     for i in range(len(candidates)):
        #         combination(candidates,temp+[candidates[i]],target)
        # combination(candidates,[],target)
        # for i in range(len(li)):
        #     li[i].sort()
        # res = list(set(map(lambda i: tuple(sorted(i)), li)))
        # for i in range(len(res)):
        #     res[i]=list(res[i])
        # return res
        def combinationSum(self, candidates, target):
            ret = []
            self.dfs(candidates, target, [], ret)
            return ret
    
        def dfs(self, nums, target, path, ret):
            if target < 0:
                return 
            if target == 0:
                ret.append(path)
                return 
            for i in range(len(nums)):
                self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
        
            
            
        