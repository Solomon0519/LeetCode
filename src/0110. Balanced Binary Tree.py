# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_tree_height(node: Optional[TreeNode]) -> bool:

            if not node:
                return 0

            left_height = check_tree_height(node.left)

            if (left_height == - 1):
                return -1

            right_height = check_tree_height(node.right)

            if (right_height == - 1):
                return - 1

            if (abs(right_height - left_height) > 1):
                return -1

            return max(left_height, right_height) + 1

        return check_tree_height(root) != -1