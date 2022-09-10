# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if  root==None:
            return False
        def dfs(s,root,flag):
            if root==None:
                return 0
            s+=root.val
            if s==targetSum and root.left==None and root.right==None:
                flag[0]=True
                return
            dfs(s,root.left,flag)
            dfs(s,root.right,flag)
        flag=[False]
        dfs(0,root,flag)
        return flag[0]