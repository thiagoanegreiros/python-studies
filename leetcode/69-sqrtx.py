class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (r + l) // 2
            m_squared = mid * mid
            if m_squared == x:
                return mid
            elif m_squared < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
    
print(Solution().mySqrt(4))
