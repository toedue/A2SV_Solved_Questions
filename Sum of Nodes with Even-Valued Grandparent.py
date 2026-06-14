# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def traverse(curr_node, parent, grand_parent):
            if not curr_node:
                return 

            if grand_parent and grand_parent.val % 2 == 0:
                self.total += curr_node.val
            
            traverse(curr_node.left, curr_node, parent)
            traverse(curr_node.right, curr_node, parent)

            

        traverse(root, None, None)
        return self.total

        
