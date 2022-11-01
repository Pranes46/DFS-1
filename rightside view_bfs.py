# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:  #TC - O(n), SC - O(n)
        
        #using BFS
        
        if not root:  #if there is no root we are returning the empty list
            return []
        
        result = []  #to store the result we are creating an empty list

        q = deque() #bfs has to be done using queue so we are initailizing deque
        
        q.append(root)   #to start the while loop we are appending the reference of the root in the queue
        
        while q:  #if the queue is empty the loop will break
            size = len(q)   #size parameter
            for i in range(size):  #iterating through each level
                
                node = q.popleft() #we are poping and storing the first element that is in queue 
                
                if node.left:  #if the node has left child we are appending it in the queue
                    q.append(node.left)
                    
                if node.right:  #if the node has right child we are appending it in the queue
                    q.append(node.right)
                    
            result.append(node.val)  #after the iteration is done we are appending the node val in the list 
            
        return result  #we are returning the list
            
        
