class Solution():
    def rotate(self, nums, k):
        k = k % len(nums)

        def aux(l, r):
           while l < r:
               nums[l], nums[r] = nums[r], nums[l]
               l +=1
               r -= 1
        
        aux(0, len(nums) - 1)
        aux(0, k - 1)
        aux(k, len(nums) - 1)
        return nums

solution = Solution()

print(solution.rotate([1,2,3,4,5,6,7], 3))