from typing import List
from time import perf_counter

def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        finish = perf_counter()
        print(f"{func.__name__} function took {finish - start} seconds to complete")
        return result
    return wrapper

@timeit
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        complement = target - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == complement:
                return [i,j]


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
