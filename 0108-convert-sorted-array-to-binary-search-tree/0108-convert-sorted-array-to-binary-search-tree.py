# Definition for a binary tree node (Provided by LeetCode automatically):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements in the current range
            if left > right:
                return None
            
            # Always pick the middle element as the root to ensure height balance
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            
            # Recursively build left and right subtrees
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
        
        return build_bst(0, len(nums) - 1)