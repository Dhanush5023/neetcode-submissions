# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
        n = len(pairs)

        for i in range(n):
            current = pairs[i]
            j = i

            while j > 0 and pairs[j - 1].key > current.key:
                pairs[j] = pairs[j - 1]
                j -= 1

            pairs[j] = current
            ans.append(pairs[:])

        return ans