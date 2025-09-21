# Height of binary tree
# https://www.geeksforgeeks.org/problems/height-of-binary-tree/1



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def height(self, root: TreeNode) -> int:
        if root is None:
            return -1 
        return 1 + max(self.height(root.left), self.height(root.right))


def build_tree(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

sol = Solution()

root1 = build_tree([12, 8, 18, 5, 11])
print("Height:", sol.height(root1)) 

root2 = build_tree([1, 2, 3, 4, None, None, 5, None, None, 6, 7])
print("Height:", sol.height(root2)) 
