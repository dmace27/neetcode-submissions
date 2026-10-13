# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node: TreeNode, parent: int, isLeftChild: bool):
            
            nonlocal res
            
            if not res:
                return

            if isLeftChild and node.val >= parent:
                res = False
                return
            elif not isLeftChild and node.val <= parent:
                res = False
                return
            
            if node.left:
                dfs(node.left, node.val, True)
            
            if node.right:
                dfs(node.right, node.val, False)
        
        if root.right:
            dfs(root.right, root.val, False)
        if root.left:
            dfs(root.left, root.val, True)

        return res
