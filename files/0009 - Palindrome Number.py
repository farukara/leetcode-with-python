#!python3
# coding = utf-8
# leetcode problem #9

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif len(str(x)) == 1:
            return True
        elif x%10 == 0:
            return False
        strx = str(x)
        for i in range(len(strx)//2):
            if strx[i] != strx[-i-1]:
                return False
        return True

sol = Solution()
tests = [121, -121, 10, -101, 234565432, 2345543, 0]
for i in tests:
    print(str(i).ljust(15, "."), sol.isPalindrome(i))
            


