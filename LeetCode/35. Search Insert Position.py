from typing import List
class Solution:
    def searchInsert(nums: List[int], target: int) -> int:
        nums.append(target)
        arr = sorted(nums)
        return arr.index(target)

ans = Solution.searchInsert([-1], 0)
print(ans)