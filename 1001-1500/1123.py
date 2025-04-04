# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return [0, None]
            
            [leftDepth, leftNode] = dfs(node.left)
            [rightDepth, rightNode] = dfs(node.right)
            if leftDepth == rightDepth:
                return [leftDepth + 1, node]
            elif leftDepth > rightDepth:
                return [leftDepth + 1, leftNode]
            else:
                return [rightDepth + 1, rightNode]
        
        return dfs(root)[1]        
