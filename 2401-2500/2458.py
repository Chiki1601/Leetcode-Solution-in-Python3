# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.h = dict()
        self.q = dict()
        self.root_h = 0
        
    def height(self, node):
        if node is None:
            return -1
        l = self.height(node.left)
        r = self.height(node.right)
        mx, mn = max(l, r), min(l, r)
        self.h[node.val] = mx + 1, mx - mn
        return self.h[node.val][0]
    
    def cal_prefix(self, node, h):
        self.q[node.val] = max(h, self.root_h - self.h[node.val][0] - 1)
        h = max(h, self.root_h - self.h[node.val][1])
        
        left_h = self.h[node.left.val][0] if node.left else -1
        right_h = self.h[node.right.val][0] if node.right else -1
        
        if left_h > right_h:
            self.cal_prefix(node.left, h)
        elif right_h > left_h:
            self.cal_prefix(node.right, h)
    
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.height(root)
        self.root_h = self.h[root.val][0]
        self.cal_prefix(root, 0)
        ans = list()
        for val in queries:
            ans.append(self.q.get(val, self.root_h))
        return ans
