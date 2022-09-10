# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        def recurse(root):
            if root is None:
                return
            else:
                li.append(root.val)
                recurse(root.left)
                recurse(root.right)
        recurse(root)
        return li
        