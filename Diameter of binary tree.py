# Diameter of binary tree
# https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/1



from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def height(node):
            if not node:
                return -1 
            
            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter, left_height + right_height + 2)
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter

from collections import deque
def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    while q and i < len(arr):
        node = q.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root

sol = Solution()

root1 = build_tree([1, 2, 3])
print("Diameter:", sol.diameterOfBinaryTree(root1)) 

root2 = build_tree([5, 8, 6, 3, 7, 9])
print("Diameter:", sol.diameterOfBinaryTree(root2)) 
