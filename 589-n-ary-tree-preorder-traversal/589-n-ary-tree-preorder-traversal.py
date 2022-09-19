"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        output = []
        
        def dfs(node):
            if not node:
                return
            output.append(node.val)
            
            for child in node.children:
                dfs(child)
        dfs(root)
        
        return output
             