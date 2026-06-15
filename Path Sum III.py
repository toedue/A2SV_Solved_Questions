# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = {0:1}

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val

            path_found = sums.get(current_sum - targetSum, 0)

            sums[current_sum] = sums.get(current_sum, 0) + 1

            path_found += dfs(node.left, current_sum)
            path_found += dfs(node.right, current_sum)

            sums[current_sum] -= 1

            return path_found

        return dfs(root, 0)
        
