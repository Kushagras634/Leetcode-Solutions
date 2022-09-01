# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(root,maxx):
            if root==None:
                    return 0
            if root.val>=maxx:
                    maxx=root.val
                    return 1+traverse(root.left,maxx)+traverse(root.right,maxx)
            return traverse(root.left,maxx)+traverse(root.right,maxx)
        return traverse(root,root.val)

            
            
        