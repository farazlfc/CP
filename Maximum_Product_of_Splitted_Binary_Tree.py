# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = self.dfs_sum(root)
        print(self.total)
        answer = self.dfs_find(root)
        return answer
        #one traversal to calulcate full sum and second for product 
    def dfs_sum(self, root):
        stack = [root]
        sum_ = 0
        while stack:
            curr = stack.pop()
            sum_ += curr.val
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return sum_
    
    def dfs_find(self, root):
        MAX = float("-inf")
        def recurse(node):
            nonlocal MAX
            if node is None:
                return 0
            SUM = node.val + recurse(node.left) + recurse(node.right)
            MAX = max(MAX, (self.total -SUM)*SUM)
            return SUM
        recurse(root)
        return MAX%(10**9 + 7)

                
