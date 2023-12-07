# LeetCode 94

class Solution:
    def inorder(self, root, outList):
        # happens when we want to visit left/right child of a node but it doesn't exist
        if root == None:
            # exist the function
            return outList
        
        # REORDERED three lines below (for different traversals, change the order accordingly)
        self.inorder(root.left, outList)
        outList.append(root.val)
        return self.inorder(root.right, outList)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        outList = []
        self.inorder(root, outList)
        return outList