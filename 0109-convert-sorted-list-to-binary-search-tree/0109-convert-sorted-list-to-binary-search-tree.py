# Definition for singly-linked list (Provided by LeetCode automatically):
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node (Provided by LeetCode automatically):
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 1. Count the total length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        self.head = head

        # 2. Build BST using In-Order Simulation
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # Step A: Build left subtree first
            left_child = build_bst(left, mid - 1)
            
            # Step B: Create current root using head node, then advance pointer
            root = TreeNode(self.head.val)
            root.left = left_child
            self.head = self.head.next
            
            # Step C: Build right subtree
            root.right = build_bst(mid + 1, right)
            
            return root

        return build_bst(0, length - 1)