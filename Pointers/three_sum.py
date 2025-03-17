"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""

class SolutionOne:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]
                if sum_val == 0:
                    result = [nums[i], nums[left], nums[right]]
                    if result not in answer:
                        answer.append(result)
                    left += 1
                    right -= 1
                elif sum_val < 0:
                    left += 1
                else:
                    right -= 1
        return answer


"""
The time complexity is O(N^2) — The twoSum function takes O(N) time because the two pointers traverse the entire array once. The outer loop runs for N iterations, and the inner loop runs for N - 1 iterations. This results in a quadratic time complexity.
The space complexity is O(1) — No additional data structures are used. The algorithm uses only a constant amount of extra space (a few integer variables for the indices and result list). The result list always has exactly three elements.

The speed is negative impacted by the check of result in answer. The check is O(n) and it is not necessary. The result can be added to answer without checking if it is already there. The sorting of the list is also not necessary.
"""


class SOlutionTwo:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]
                if sum_val == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_val < 0:
                    left += 1
                else:
                    right -= 1
        return answer


"""
The time complexity is O(N^2) — The twoSum function takes O(N) time because the two pointers traverse the entire array once. The outer loop runs for N iterations, and the inner loop runs for N - 1 iterations. This results in a quadratic time complexity.
The space complexity is O(1) — No additional data structures are used. The algorithm uses only a constant amount of extra space (a few integer variables for the indices and result list). The result list always has exactly three elements.
The speed is improved by removing the check of result in answer. The check is O(n) and it is not necessary. The result can be added to answer without checking if it is already there. The sorting of the list is also not necessary.
"""