'''
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

#Solution

def val_anag(s,t):
    if len(s) != len(t):
        return False
    countS,countT = {},{}
    for i in range(len(s)):
        countS[[i]] = 1 + countS.get(s[i],0)
        countT[[i]] = 1 + countT.get(t[i],0)
    for num in countS:
        if countS[num] != countT(num,0):
            return False
    return True

'''
    The time complexity is O(n) where n is the lenght of string. The space complexity is O(k) where k is the number of unique string characters.
'''