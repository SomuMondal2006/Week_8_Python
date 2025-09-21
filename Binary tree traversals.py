# Binary tree traversals
# https://www.geeksforgeeks.org/problems/inorder-traversal/1



from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        current = root

        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right

                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    result.append(current.val)
                    current = current.right

        return result

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

root1 = build_tree([1, 2, 3, 4, 5])
sol = Solution()
print("Inorder Traversal:", sol.inorderTraversal(root1)) 

root2 = build_tree([8, 1, 5, None, 7, 10, 6, None, 10, 6])
print("Inorder Traversal:", sol.inorderTraversal(root2))  
