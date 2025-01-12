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
        # go through and just keep a set of all elements seen so far until you get to the desired values
        # remove...no idfk. UGH.
        # Go through, label each node with its parent node.
        # Then find the p and q nodes.
        # Then, from the p and q nodes, take a step upwards one at a time, keeping sets of seen values.
        # For each step, if the p-parent node is in the q set already, that's the LCA, and vice versa.

        # So...first step is to do a DFS that returns the tree ig...
        p_dfs = self.dfs(root, p.val, [])
        q_dfs = self.dfs(root, q.val, [])
        print("p_dfs:")
        for node in p_dfs:
            print(node.val)

        print("\nq_dfs:")
        for node in q_dfs:
            print(node.val)

        i = 0
        while p_dfs[i].val == q_dfs[i].val:
            i += 1

        return p_dfs[i - 1]

     

    def dfs(self, root, target, arr):
        if root == None:
            return None
        if root.val == target:
            return arr
        else:
            left = self.dfs(root.left, target, arr + [root]) 
            if left != None:
                return left + [root.left]
            right = self.dfs(root.right, target, arr + [root])
            if right != None:
                return right + [root.right]
            return None

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
