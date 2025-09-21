# Insert node in BST
# https://www.geeksforgeeks.org/problems/insert-a-node-in-a-bst/1



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insertIntoBST(root.left, key)
        elif key > root.val:
            root.right = self.insertIntoBST(root.right, key)
        return root

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

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

sol = Solution()

root1 = build_tree([2, 1, 3])
root1 = sol.insertIntoBST(root1, 4)
print("In-order after insertion:", inorder(root1)) 

root2 = build_tree([2, 1, 3, None, None, None, 6])
root2 = sol.insertIntoBST(root2, 4)
print("In-order after insertion:", inorder(root2)) 

root3 = build_tree([2, 1, 3])
root3 = sol.insertIntoBST(root3, 2)
print("In-order after insertion:", inorder(root3)) 
