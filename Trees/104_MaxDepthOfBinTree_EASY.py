# LeetCode 104
# Top-Down Solution

class Solution:
    max_depth = 0
    def topDown(self, node, depth):
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            self.max_depth = max(self.max_depth, depth)

        left_ans = self.topDown(node.left, depth+1)
        right_ans = self.topDown(node.right, depth+1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.topDown(root, 1)
        return self.max_depth