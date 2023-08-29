from typing import List
class Solution:
    def plusOne(digits: List[int]) -> List[int]:
        number = int(''.join(str(i) for i in digits)) + 1
        updated = [int(j) for j in list(str(number))]
        return list(updated)
    
ans = Solution.plusOne([0,1,2,4,9])
print(ans)