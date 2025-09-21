# Mirror of binary tree
# https://www.geeksforgeeks.org/problems/mirror-tree/1



from collections import deque

class Node:
    def __init__(self, val=0):
        self.data = val
        self.left = None
        self.right = None

def mirror(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    mirror(root.left)
    mirror(root.right)
    
    return root

def build_tree(arr):
    if not arr or arr[0] is None:
        return None
    
    root = Node(arr[0])
    q = deque([root])
    i = 1
    
    while q and i < len(arr):
        node = q.popleft()
        
        if i < len(arr) and arr[i] is not None:
            node.left = Node(arr[i])
            q.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = Node(arr[i])
            q.append(node.right)
        i += 1
    
    return root

def level_order(root):
    if not root:
        return []
    
    result = []
    q = deque([root])
    
    while q:
        node = q.popleft()
        if node:
            result.append(node.data)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()
    
    return result

arr1 = [1, 2, 3, None, None, 4]
root1 = build_tree(arr1)
mirror(root1)
print("Mirror Tree (Example 1):", level_order(root1))  

arr2 = [1, 2, 3, 4, 5]
root2 = build_tree(arr2)
mirror(root2)
print("Mirror Tree (Example 2):", level_order(root2)) 
