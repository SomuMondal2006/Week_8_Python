# Delete node in BST
# https://www.geeksforgeeks.org/problems/delete-a-node-from-bst/1



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
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
root1 = sol.deleteNode(root1, 12)
print("In-order after deletion:", inorder(root1)) 

root2 = build_tree([1, None, 2, None, 8, 5, 11, 4, 7, 9, 12])
root2 = sol.deleteNode(root2, 11)
print("In-order after deletion:", inorder(root2)) 

root3 = build_tree([2, 1, 3])
root3 = sol.deleteNode(root3, 3)
print("In-order after deletion:", inorder(root3))  
