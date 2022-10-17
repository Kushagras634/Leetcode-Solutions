class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr.count(1)==len(arr)-1:
            return True
        visited=[]
        def dfs(arr,i):
            if i>len(arr)-1 or i<0:
                return False
            if arr[i]==0:
                
                return True
            else:
                if i+arr[i] not in visited and i-arr[i] not in visited:
                    visited.append(i+arr[i])
                    visited.append(i+arr[i])
                    return dfs(arr,i+arr[i]) or dfs(arr,i-arr[i])
                if i+arr[i] not in visited:
                    visited.append(i+arr[i])
                    return dfs(arr,i+arr[i])
                if i-arr[i] not in visited:
                    visited.append(i-arr[i])
                    return dfs(arr,i-arr[i])
                
        return dfs(arr,start)
        
        
        
        