#1 Simple. Distinguish ‘no root’ and 'no child’.

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

#2 Too complicated. Don’t overthink

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        n = 0
        if not root:
            return 0
        if not root.left and not root.right:
            n = 1
        if root.left and not root.right:
            n = self.maxDepth(root.left) + 1
        if root.right and not root.left:
            n = self.maxDepth(root.right) + 1
        if root.left and root.right:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return n
