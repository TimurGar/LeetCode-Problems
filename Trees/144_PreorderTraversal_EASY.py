#LeetCode 144
# Recursively

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

 
# Iteratively
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        res = []

        while curr or stack:
            if curr:
                res.append(curr.val)
                # saving the right child before going to the left child
                # this way, we don't lose access to the right child
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return res
