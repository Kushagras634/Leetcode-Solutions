# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        roots=[]
        def recurse(root,roots):
            if root is None:
                return
            recurse(root.left,roots)
            roots.append(root.val)
            recurse(root.right,roots)
        recurse(root,roots)
        for i in range(1,len(roots)):
            if roots[i-1]>=roots[i]:
                return False
        return True
            
        