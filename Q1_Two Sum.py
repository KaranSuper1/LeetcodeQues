# Solution
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for k in range(len(nums)-1):
            for i in range(k,len(nums)-1):
                if nums[k] + nums[i + 1] == target:
                    return [i, i + 1]

# Test
a=Solution()
print(a.twoSum([3,2,4],6))