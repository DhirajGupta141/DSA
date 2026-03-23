
"""
Approach : 

if its rotated and sorted then there will be one drop point where a[i] > a[i+1]
there should not be more than one 

thats why we have count <= 1

"""
from typing import List

class Solution:
    def check(self, a: List[int]) -> bool:
        
        n = len(a)
        count = 0 
        for i in range(n-1):
            if a[i] > a[i+1]:
                count += 1 

        # last element should be greater than first element 
        if a[-1] > a[0]:
            count += 1
        
        return count <= 1 


        
       


        