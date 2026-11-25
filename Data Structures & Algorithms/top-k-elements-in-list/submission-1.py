class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = {}

        for num in nums:
            if num in heap:
                heap[num] += 1
            else:
                heap[num] = 1

        result = sorted(heap, key=heap.get, reverse=True)
        return result[:k]