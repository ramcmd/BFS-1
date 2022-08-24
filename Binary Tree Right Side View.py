# TC: O(n)
# SC: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        q = deque()
        
        if root == None:
            return result
        else:
            q.append(root)
            
        while q:
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # logic : first you seach weather you have left node, append in the queue.
            # then you append the right node to the queue
            # append the last element.val into the result 
            # if it exists, it exists, else: left node will be taken
            result.append(node.val)
            
        return result