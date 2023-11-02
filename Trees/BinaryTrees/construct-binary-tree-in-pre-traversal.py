# Given two integer arrays preorder and inorder where preorder
# is the preorder traversal of a binary tree and inorder is the 
# inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        left = 0
        right = len(preorder)
        self.current = 0
        def constructTree(preorder, inorder, left, right):
            if(left > right):
                return None

            if(self.current == len(preorder)):
                return None
                
            nodeVal = preorder[self.current]
            node = TreeNode(nodeVal)
            self.current = self.current+1
            
            if(left == right):
                return node
            
            idx = inorder.index(nodeVal, left, right+1)

            #for left
            node.left = constructTree(preorder, inorder, left, idx-1)

            #for right
            node.right = constructTree(preorder, inorder, idx+1, right)

            return node

        return constructTree(preorder, inorder, left, right)


