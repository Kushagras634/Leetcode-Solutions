# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def vert(root,ht,i,j):
            if root is None:
                return
            vert(root.left,ht,i+1,j-1)
            if j in ht:
                ht[j].append([i,root.val])
            else:
                ht[j]=[]
                ht[j].append([i,root.val])
            vert(root.right,ht,i+1,j+1)
        dic={}
        
        vert(root,dic,0,0)
        result = []
        for i in sorted(dic.keys()):
            temp = []
            for j in sorted(dic[i]):
                temp.append(j[1])
            result.append(temp)
        return result
        
        
        