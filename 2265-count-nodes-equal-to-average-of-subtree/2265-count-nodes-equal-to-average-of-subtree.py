# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []

        def postorder(node):
            if not node:
                return 

            postorder(node.left)
            postorder(node.right)
            nodes.append(node)
        
        postorder(root)

        info = {}

        ans = 0

        for node in nodes:
            left_sum, left_count = info.get(node.left, (0, 0))
            right_sum, right_count = info.get(node.right, (0, 0))

            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            average = subtree_sum // subtree_count

            if average == node.val:
                ans += 1

            info[node] = (subtree_sum, subtree_count)
        
        return ans