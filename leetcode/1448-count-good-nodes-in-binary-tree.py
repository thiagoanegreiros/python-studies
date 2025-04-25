class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def aux(root, max_so_far):
            if root is None:
                return 0

            count = 1 if root.val >= max_so_far else 0
            max_so_far = max(max_so_far, root.val)

            count += aux(root.left, max_so_far)
            count += aux(root.right, max_so_far)

            return count

        return aux(root, root.val)

print(Solution().goodNodes(build_tree([3,1,4,3,None,1,5])))
