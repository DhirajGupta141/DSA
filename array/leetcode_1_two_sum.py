from typing import List

class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:

        n = len(a)
        seen = dict() # {arrayElement : index}
        for i , ele in enumerate(a):
            diff = target - ele
            if diff in seen:
                return [seen.get(diff), i]
            else:
                seen[ele] = i
            
        return []





















        