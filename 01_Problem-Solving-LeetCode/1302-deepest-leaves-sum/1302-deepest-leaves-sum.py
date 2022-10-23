class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def depth(root):
            return 1 + max(depth(root.left), depth(root.right)) if root else 0

        self.maxDepth = depth(root)
        self.res = 0

        def solve(root, d):
            if not root: return
            if d == self.maxDepth:
                self.res += root.val
            solve(root.left, d+1)
            solve(root.right, d+1)

        solve(root, 1)
        return self.res