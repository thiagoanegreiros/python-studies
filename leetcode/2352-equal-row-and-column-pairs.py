from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        hash = {}
        
        for i in range(n):
            r = tuple(grid[i]) 
            print(r)
            hash[r] = hash.get(r, 0) + 1

        print('---')

        for i in range(n):
            c = tuple([grid[r][i] for r in range(n)])
            print(c)
            count += hash.get(c, 0)

        return count

print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
