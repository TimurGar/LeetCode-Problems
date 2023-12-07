# LeetCode 102

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        if root is None:
            return []
        
        queue = [root]
        res = []

        while queue:
            current_level = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)

                # adding children to the queue (for the next iteration)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(current_level)
        
        return res
