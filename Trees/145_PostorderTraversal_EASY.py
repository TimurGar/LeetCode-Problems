# LeetCode 145

class Solution:
    def postorder(self, root, outList):
        # happens when we want to visit left/right child of a node but it doesn't exist
        if root == None:
            # exist the function
            return outList

        # REORDERED three lines below (for different traversals, change the order accordingly)
        self.postorder(root.left, outList)
        self.postorder(root.right, outList)
        return outList.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        outList = []
        self.postorder(root, outList)
        return outList