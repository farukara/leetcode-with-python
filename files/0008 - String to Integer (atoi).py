#!python3
#coding = utf-8
#leetcode - 8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if s[0] == "-":
            s = s[1:]
            if s:
                if not s[1].isnumeric():
                    return 0
                number = ""
                for digit in s[1:]:
                    if digit.isnumeric():
                        number += digit
                    else:
                        break
                if not number:
                    return 0
                else:
                    number = int(number)
                    if number > 2147483648:
                        return -2147483648
                    else:
                        return number*(-1)
            else:
                return 0

        else:
            if s[0] == "+":
                s = s[1:]
            if s:
                number = ""
                for digit in s:
                    if digit.isnumeric():
                        number += digit
                    else:
                        break
                if not number:
                    return 0
                else:
                    number = int(number)
                    if number > 2147483647:
                        return 2147483647
                    return number
            else:
                return 0

sol = Solution()
numbers = ["42", "-42", "4193 with words", "words and 987", "-91283472332", "2147483649",  "71147483649",  "-71147483649", "-91283472332", "", "+1", " "]
for number in numbers:
    print(number ," : ", sol.myAtoi(number))
