'''
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
from collections import defaultdict


def group_anagrams(strs: str):
    res = defaultdict(list)
    for s in strs:
        arr = [0] * 26
        for x in s:
            arr[ord(x) - ord("a")] += 1
        res[tuple(arr)].append(s)
    return res.values()

'''
    Time complexity of the group_anagrams function is O(n * m), where n is the total number of strings in the input list 'strs', 
    and m is the maximum length of a string in 'strs'.
    Space complexity of the function is O(n * m) because the function uses a dictionary 'res' to store the grouped anagrams.
'''