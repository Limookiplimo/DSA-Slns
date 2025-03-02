'''
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    
'''

# Solution:

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        elems = set()
        for elem in nums:
            if elem in elems:
                return True
            elems.add(elem)
        return False
    
'''
    Time complexity is O(1) since sets have a contant-time lookup.
    Incase there are no duplicates (worst case scenario), the space complexity is O(n).
'''