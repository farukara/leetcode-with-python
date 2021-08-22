#!python3
# coding = utf-8

from time import perf_counter

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(f"{func.__name__} function took {finish - start} seconds to complete")
        return result
    return wrapper

def in_binary_search(array, item):
    "returns True if item in unsorted array, False otherwise"
    array.sort()
    if len(array) == 1:
        if array[0] == item:
            return True
        return False
    midpoint = len(array)//2
    lhalf = array[:midpoint]
    rhalf = array[midpoint:]
    return in_binary_search(lhalf, item) or in_binary_search(rhalf, item)

class Solution:
    @timeit
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            if in_binary_search(nums[i+1:], complement):
                return [i, nums[i+1:].index(complement)+i+1]

sol = Solution()
nums = [2,7,11,15]
nums = [3,3]
target = 6
print(sol.twoSum(nums, target))
