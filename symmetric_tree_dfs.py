# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        
        
        result = []  #creating a result array to store the result
        self.dfs(root,0,result)  #calling and passing root, level and result in the recurrsion
        
        for node in result:   #we are doing palindrome check whether it is symettric or not
            if not self.ispalindrome(node):
                return False  #if the palindrome function returns false it returns false else true
            
        return True
       
            
        
    def dfs(self,root,level,result):  #recurrsion function
        
        if len(result) < level+1: #if the len of result is sammler than the level+1 we are creating a list
            result.append([ ]) 
        if root:   #if root has a value we are appending it into the result
            result[level].append(root.val) 
        else:   #if root doesnt have value we are appending None
            result[level].append(None) 
        if root: #if root has value we are calling the recurssion fuinction
            self.dfs(root.left,  level+1,result)   
            self.dfs(root.right, level+1,result)
            
    def ispalindrome(self,li):  #palindrome check
        left = 0  #left pointer at index 0
        right = len(li)-1  #right pointer at end of the list
        
        while left<=right:  #the loop will break once the left pointer crosses thr right pointer
            if li[left]!=li[right]:  #if the left value and rioght value is not equal it is not palindrome so we are returning false
                return False
            
            left+=1  #we are increasing the left pointer
            right-=1  #we are decreasing the right pointer
                
        return True  #if it is palindrome we are returning True
        
        
        
        
       
        
        
        
        