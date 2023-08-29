from typing import List
class Solution:
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1 = nums1[0:m]
        nums1.extend(nums2[0:n])
        nums1.sort()
        return nums1
ans = Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(ans)