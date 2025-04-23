from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False
    
print(Solution().increasingTriplet([1,2,3,4,5]))
print(Solution().increasingTriplet([2,1,5,0,4,6]))
