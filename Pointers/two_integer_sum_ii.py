"""
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
There will always be exactly one valid solution.
Your solution must use O(1) additional space.
"""


class SolutionOne:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

    """
    The worst case time complexity is O(n^2)). The outer loop runs n times (where n is the length of numbers). The inner loop runs approximately n - i - 1 times. 
    In the best case, where the solution is found at the first pair, the complexity is O(1).
    The space complexity is O(1) since the algorithm only uses a fixed-size list of two elements ([i + 1, j + 1]) for the result. No additional data structures are used.
    """

class SolutionTwo:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index1, index2 = 0, len(numbers) - 1
        while index1 < index2:
            sum_val =  numbers[index1] + numbers[index2]
            if sum_val > target:
                index2 -= 1
            elif sum_val < target:
                index1 += 1
            else:
                return [index1 + 1, index2 + 1]
        return []
   
    """
    The time complexity is O(N) — Worst case, the two pointers traverse the entire array once. The while loop iterates at most N times, where N is the length of the numbers list.
    In each iteration, the algorithm either moves the left pointer index1 forward or the right pointer index2 backward — this guarantees that the pointers never move back, making the loop linear.
    The space complexity is O(1) — No additional data structures are used. The algorithm uses only a constant amount of extra space (a few integer variables for the indices and result list). The result list always has exactly two elements.
    """
