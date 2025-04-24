from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = cur = prev = 0

        for bit in nums:
            if bit:
                cur += 1
                longest = max(longest, cur + prev)
            else:
                prev, cur = cur, 0
        
        return longest - (longest == len(nums))


print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
