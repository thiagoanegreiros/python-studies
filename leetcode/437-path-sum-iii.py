class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum_count = {0: 1}
        def dfs(node, current_sum):
            if node is None:
                return 0

            current_sum += node.val

            num_paths = prefix_sum_count.get(current_sum - targetSum, 0)

            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

            num_paths += dfs(node.left, current_sum)
            num_paths += dfs(node.right, current_sum)

            prefix_sum_count[current_sum] -= 1

            return num_paths
        
        return dfs(root, 0)

print(Solution().pathSum(build_tree([10,5,-3,3,2,None,11,3,-2,None,1]), 8))