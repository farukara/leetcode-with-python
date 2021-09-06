#!python3
#coding=utf-8
#leetcode 14. Longest Common Prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        common = ""
        base = min(strs, key=len)
        for string in strs:
            common = ""
            for j in range(len(base)):
                if base[j] == string[j]:
                    common += base[j]
                else: 
                    break
            if not common:
                break
            else:
                base = common
        return common

sol = Solution()
inputs = [["flower","flow","flight"], ["dog","racecar","car"], [""], ["a"], ["acc","aaa","aaba"]]
for input in inputs:
    print(sol.longestCommonPrefix(input))
