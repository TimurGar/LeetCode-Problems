#LeetCode 112

class Solution:
    def topDown(self, node, currSum, targetSum):
        if node is None:
            return False
        
        currSum += node.val
        print("Curr Sum: ", currSum)
        if not node.left and not node.right:
            if currSum == targetSum:
                return True
            else:
                # We don't need to substract the node.val from cussSum as currSum doesn't              
                # is a local variable (only true/false is returned when the leaf is reached)
                return False

        return (self.topDown(node.left, currSum, targetSum) or
                self.topDown(node.right, currSum, targetSum)) 

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.topDown(root, 0, targetSum)
