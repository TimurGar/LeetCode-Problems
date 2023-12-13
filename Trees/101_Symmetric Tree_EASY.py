# LeetCode 101

class Solution:

    def dfs(self, left, right):
        # Node with no children
        if not left and not right:
            return True
        # Node with only one child
        if not left or not right:
            return False

        # comparing left and right substrees
        return (left.val == right.val and
                # comparing left child of the left subree (inEx 3) to right child of right subtree (in Ex 3)
               self.dfs(left.left, right.right) and 
               self.dfs(left.right, right.left)) # 'inner' children (4 to 4)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root.left, root.right)