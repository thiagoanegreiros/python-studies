class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mhash = {}
        for i in magazine:
            mhash[i] = mhash.get(i, 0) + 1
        
        for i in ransomNote:
            h_value = mhash.get(i, 0)
            if h_value == 0:
                return False
            elif h_value == 1:
                del mhash[i]
            else:
                mhash[i] = h_value - 1

        return True
            

print(Solution().canConstruct('aa', 'aab'))
