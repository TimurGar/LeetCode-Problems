#LeetCode 144

class Solution:

    def preorder(self, root, outList):
        # happens when we want to visit left/right child of a node but it doesn't exist
        if root is None: 
            # exist the function
            return  

        outList.append(root.val) # appending root
        self.preorder(root.left, outList) # visitin left
        return self.preorder(root.right, outList) # visiting right

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        outList = []
        self.preorder(root, outList)
        return outList