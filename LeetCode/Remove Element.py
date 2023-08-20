from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = nums.count(val)
        for i in range(0,count):
            nums.remove(val)
        nums[:] = sorted(nums)
        return len(nums)
print(Solution.removeElement([3,2,2,3], 3))