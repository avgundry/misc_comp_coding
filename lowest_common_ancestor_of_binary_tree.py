# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val

    def __str__(self):
        return str(self.val)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pFound = False
        qFound = False

        self.dfs(root, p.val, q.val, pFound, qFound)

        if root == None:
            return 0
        elif root.val == p.val:
            return 2

    def dfs(self, root, p, q, pFound, qFound):
        if root is None:
            return False
        elif root.val == p:
            if qFound:
                return root
            pFound = True
        elif root.val == q:
            if pFound:
                return root
            qFound = True

            return self.dfs(root.left, target) or self.dfs(root.right, target)

if __name__ == "__main__":
    root = TreeNode(3, 
                    TreeNode(5, 
                             TreeNode(6),
                             TreeNode(2,
                                      TreeNode(7),
                                      TreeNode(4)
                                      ),
                            ),
                    TreeNode(1,
                             TreeNode(0),
                             TreeNode(8)
                            )
                    )

    p = TreeNode(5)
    q = TreeNode(1)
    s = Solution()
    print('\nSolution:\n')
    print(s.lowestCommonAncestor(root, p, q))
