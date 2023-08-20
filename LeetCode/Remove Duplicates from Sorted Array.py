from typing import List
class Solution:
    def removeDuplicates(nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
    
print(Solution.removeDuplicates([1,1,2]))