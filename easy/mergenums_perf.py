from _performance import compare_speed, visualize_speed
import random

def mergeIntNums(nums: list):
    return sum(nums[len(nums)-i-1] * 10 ** (i) for i in range(len(nums)))
    
def mergeStrNums(nums: list):
    return mergeIntNums([int(nums) for nums in nums])

def mergeStrNumsBuiltIn(nums: list):
    return int("".join(nums))

print(mergeIntNums([4,5,6,8]))

inputs = [
    [[str(random.randint(1,9)) for i in range(random.randint(1,9))]]
    for calls in range(10000)
]
inputAsKeyLambda = lambda x: mergeStrNumsBuiltIn(x[0])
fnList = [mergeStrNums, mergeStrNumsBuiltIn]
time_dict = compare_speed(fnList, inputs, inputAsKeyLambda=inputAsKeyLambda)
visualize_speed(fnList, time_dict)