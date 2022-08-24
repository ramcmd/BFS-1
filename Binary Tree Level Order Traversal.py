# TC: O(n)
# SC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        result = []
        
        if root == None:
            return result
        else:
            q.append(root)
        
        while q:
            temp = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                temp.append(node.val)
            
            result.append(temp)
        
        return result
            
            
            
        
    
   