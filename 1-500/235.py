class Solution:

    def lowestCommonAncestor(self, root, p, q):

        """

        :type root: TreeNode

        :type p: TreeNode

        :type q: TreeNode

        :rtype: TreeNode

        """

        # approach: compare current node with p and q, then move

        #           current to it’s left or right child by result

        current = root

        while root:

            if root.val > p.val and root.val > q.val:

                root = root.left

            elif root.val < p.val and root.val < q.val:

                root = root.right

            else: break

        return root
