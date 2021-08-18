#!python3
#coding = utf-8
#leetcode - 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        upper_limit = pow(2,31)-1
        lower_limit = pow(-2,31)
        if x == 0:
            return 0
        elif x < 0:
            reversed = int(str(x)[1:][::-1])
            if reversed >= upper_limit and -reversed <= lower_limit:
                return 0
            else:
                return -reversed
        else:
            reversed = int(str(x)[::-1])
            if reversed >= upper_limit:
                return 0
            else:
                return reversed

sol = Solution()
numbers = [123, -123, 120, 0, 1534236469]
for number in numbers:
    print(sol.reverse(number))
