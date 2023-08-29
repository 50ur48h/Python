#### O(n^3) time Complexity ####
# from typing import List
# class Solution:
#     def threeSum(nums: List[int]) -> List[List[int]]:
#         output = []
#         num = []
#         for i in range (0, len(nums)):
#             for j in range (i, len(nums)):
#                 for k in range (j, len(nums)):
#                     if i != j and i != k and j != k:
#                         if (nums[i] + nums[j] + nums[k]) == 0:
#                             triplet = [nums[i], nums[j], nums[k]]
#                             triplet.sort()
#                             if triplet not in output:
#                                 output.append(triplet)
#         return output
    

#### O(n^2) time complexity ####
from typing import List
class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output

op = Solution.threeSum([-12,0,6,-13,-7,-15,-6,-6,-2,-14,-2,14,1,11,-12,-11,-2,-6,7,2,-5,-9,-11,-13,9,-7,-8,9,-12,-1,5,14,14,-3,8,14,-3,-13,-14,3,10,-1,2,-3,-13,-3,-7,-7,-2,-15,2,8,-9,7,2,8,7,2,2,11,-14,-8,2,7,-4,-5,7,9,-11,0,-11,-15,14,6,-11,9,-11,-3,9,-6,-11,-4,-12,-4,10,5,11,-5,-8,-2,13,-7,-3,0,-14,1,10,0,-5,6,-15,-1,6,6])
print(op)