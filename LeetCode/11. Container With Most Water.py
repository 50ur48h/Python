from typing import List

############# Iteration Start #############
# class Solution:
#     def maxArea( height: List[int]) -> int:
#         max_water = 0
#         for currentindex in range(0,len(height)):
#             for j in range(0,len(height)):
#                 if j != currentindex:
#                     if height[j] >= height[currentindex]:
#                         if currentindex > j:
#                             water = height[currentindex]*(currentindex-j)
#                         else:
#                             water = height[currentindex]*(j-currentindex)
#                         if water > max_water:
#                             max_water = water
#         return max_water
############# Iteration End #############

############ Recursion Start ############
class Solution:
    def maxArea(height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
############ Recursion End ############

ans = Solution.maxArea([1,8,6,2,5,4,8,3,7])
print(ans)
