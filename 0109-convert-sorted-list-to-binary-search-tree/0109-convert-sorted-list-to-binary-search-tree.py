class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        self.head = head
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            left_child = build_bst(left, mid - 1)
            root = TreeNode(self.head.val)
            root.left = left_child
            self.head = self.head.next
            root.right = build_bst(mid + 1, right)
            return root
        return build_bst(0, length - 1)