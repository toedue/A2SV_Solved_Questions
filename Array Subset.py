#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    
    def isSubset(self, a, b):
        # Your code here
        
        return (Counter(b) <= Counter(a))
        
        
    
    
    
    
