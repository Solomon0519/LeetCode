# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ancestors_of_p = []
        ancestors_of_q = []

        def populate_ancestors(parent: 'TreeNode', child: 'TreeNode', ancestors: List[int], depth: int) -> None:

            parent_value = parent.val
            child_value = child.val

            ancestors.append((parent_value, depth))

            if parent_value == child_value:
                return
            elif parent_value < child_value:
                populate_ancestors(parent.right, child, ancestors, depth + 1)
            else:
                populate_ancestors(parent.left, child, ancestors, depth + 1)

        populate_ancestors(root, p, ancestors_of_p, 0)
        populate_ancestors(root, q, ancestors_of_q, 0)

        print(ancestors_of_p)
        print(ancestors_of_q)

        ancestors_of_p = set(ancestors_of_p)
        min_common_ancestor = float('inf')
        max_depth = -float('inf')

        for ancestor in ancestors_of_q:
            if ancestor in ancestors_of_p:
                if (ancestor[1] >= max_depth):
                    max_depth = ancestor[1]
                    min_common_ancestor = ancestor[0]
                else:
                    continue


        return TreeNode(min_common_ancestor)