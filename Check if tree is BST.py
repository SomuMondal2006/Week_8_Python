# Check if tree is BST
# https://www.geeksforgeeks.org/problems/check-for-bst/1



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBST(self, root: TreeNode) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)
        
        return helper(root, float('-inf'), float('inf'))

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

root1 = build_tree([2, 1, 3, None, None, None, 5])
print(sol.isBST(root1)) 

root2 = build_tree([2, None, 7, None, 6, None, 9])
print(sol.isBST(root2)) 

root3 = build_tree([10, 5, 20, None, None, 9, 25])
print(sol.isBST(root3)) 
