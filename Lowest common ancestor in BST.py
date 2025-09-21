# Lowest common ancestor in BST
# https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, n1: int, n2: int) -> TreeNode:
        while root:
            if n1 < root.val and n2 < root.val:
                root = root.left
            elif n1 > root.val and n2 > root.val:
                root = root.right
            else:
                return root
        return None

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

root1 = build_tree([5, 4, 6, 3, None, None, 7, None, None, None, 8])
lca1 = sol.lowestCommonAncestor(root1, 7, 8)
print("LCA (Example 1):", lca1.val)  

root2 = build_tree([20, 8, 22, 4, 12, None, None, None, None, 10, 14])
lca2 = sol.lowestCommonAncestor(root2, 8, 14)
print("LCA (Example 2):", lca2.val) 

root3 = build_tree([2, 1, 3])
lca3 = sol.lowestCommonAncestor(root3, 1, 3)
print("LCA (Example 3):", lca3.val) 
