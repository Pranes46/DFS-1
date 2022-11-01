"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:     #TC - O(n), SC - O(n)
        
        
        self.totalImportance = 0  #to store the total importance of the given node
        self.adj = {}  #the adjacency list
        
        for emp in employees:  #to append the key,val pair in the adjacency list
            self.adj[emp.id]  = [emp.importance, emp.subordinates]  #employee node will have id, importance and its subordinates. we are appending it in the adjacency list 
            
        self.dfs(id) #calling the recurrsion function, here we are using dfs
        
        return self.totalImportance  #returning the total imp
        
    def dfs(self, employee):  #dfs recursion
        self.totalImportance += self.adj[employee][0]  #we are calculating the total important for the employee
        
        for subordinate in self.adj[employee][1]: #if the emeployee has subordinate we are passing it in the recurrsion, likewise the recursion will flow
            self.dfs(subordinate)
            
        return  #after that we are unfolding the function

        
