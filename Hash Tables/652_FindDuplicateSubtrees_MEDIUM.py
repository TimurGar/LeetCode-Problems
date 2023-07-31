# Doesn't run on VS code
# Solution copied from online, I haven't learn dfs yet 

from collections import defaultdict

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root):
        subtrees = defaultdict(list)
        
        # doing a depth first search (preorder), to go through each node
        def dfs(node) :
            if not node:
                return "null"
            
            # creating a serialization (custom key) for each node 
            s = ",". join([str(node.val), dfs(node.left), dfs(node.right)])
        
            # to only add duplicate node once to the res, we check the len
            if len(subtrees[s]) == 1:
                res.append(node)

            # mapping the serialization of a specific node to that node
            subtrees[s].append(node)
            return s
    
        res = []
        dfs(root)
        return res
            
testSolution = Solution()
print(testSolution.findDuplicateSubtrees([1,2,3,4,"null",2,4,"null","null",4]))