"""
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
"""
# ensure the character is alphanumeric
# at comparison apply lower case
# return true or false

# Initial solution
class SolutionOne:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for c in s:
            if c.isalnum():
                new_string += c.lower()
        return new_string == new_string[::-1]

    
s = "Was it a car or a cat I saw?"
solution = SolutionOne()
print(solution.isPalindrome(s))


# Optimized solution
class SolutionTwo:
    def alphanumeric_check(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanumeric_check(s[l]):
                l += 1
            while r > l and not self.alphanumeric_check(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

s = "Was it a car or a cat I saw?"
solution = SolutionTwo()
print(solution.isPalindrome(s))