from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        last = ''
        count = 0
        stack = []
        for c in chars:
            if c != last:
                if last == '':
                    last = c
                    count = 1
                else:
                    stack.append(last)
                    if count > 1:
                        stack.extend(list(str(count)))
                    last = c
                    count = 1
            else:
                count += 1

        stack.append(last)
        if count > 1:
            stack.extend(list(str(count)))

        result = len(stack)

        chars[:] = stack

        return result

print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a"]))
