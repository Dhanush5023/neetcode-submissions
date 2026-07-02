class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # Count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort after counting everything
        arr = sorted(freq.items(), key=lambda x: x[1])

        ans = []

        # Take last k elements
        for i in range(len(arr) - k, len(arr)):
            ans.append(arr[i][0])

        return ans