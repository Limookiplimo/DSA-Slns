'''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
'''
#Solution

def two_sum(nums,target):
    numsMap = {}
    for ind, val in enumerate(nums):
        sub_val = target - val
        if sub_val in numsMap:
            return (numsMap[sub_val],ind)
        numsMap[val] = ind

'''
    The time complexity is O(n), where n is the number of elements in the nums list. 
    The space complexity is O(n) because the function uses a dictionary (numsMap) to store the numbers from the nums list along with their indices.
'''