from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        solution = {}
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i] + nums[j]
                if k == target:
                    solution[i] = nums[i]
                    solution[j] = nums[i+1]
        return solution.keys()

lss = Solution.twoSum([3,2,3], 6)
print(lss)