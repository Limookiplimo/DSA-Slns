'''
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

# Solution

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for x in range(len(nums) + 1)]
    res = []

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)
    for i in range(len(freq) - 1, 0 -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
        
'''
    Overall time complexity of the function is O(n), where n is the length of the nums list. While the space complexity is  is O(n + k),
    where n is the length of the nums list and k is the number of top frequent elements to return.
'''