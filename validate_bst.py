from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root.left, -float('inf'), root.val) and self.validate(root.right, root.val, float('inf'))

    def validate(self, root, min, max):
        if root:
            if root.val <= min or root.val >= max:
                return False
            return self.validate(root.left, min, root.val) and self.validate(root.right, root.val, max)

        return True

    
        