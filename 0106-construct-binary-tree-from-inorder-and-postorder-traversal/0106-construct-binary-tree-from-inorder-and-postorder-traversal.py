# Definition for a binary tree node (Provided by LeetCode automatically):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        # Hash map for O(1) index lookup in the inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Start from the last element of postorder array (Root of tree)
        post_idx = len(postorder) - 1

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal post_idx
            
            # Base case: no elements in this sub-range
            if left > right:
                return None

            # 1. Pick current root value from postorder traversal
            root_val = postorder[post_idx]
            root = TreeNode(root_val)
            post_idx -= 1

            # 2. Find root's position in inorder array
            inorder_idx = inorder_map[root_val]

            # 3. CRUCIAL: Build RIGHT subtree first, then LEFT subtree!
            # Since postorder is [Left -> Right -> Root], processing backwards 
            # yields [Root -> Right -> Left].
            root.right = build(inorder_idx + 1, right)
            root.left = build(left, inorder_idx - 1)

            return root

        return build(0, len(inorder) - 1)