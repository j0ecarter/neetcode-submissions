import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        # count frequencies
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # pick the k numbers (keys) with the largest counts
        return heapq.nlargest(k, counts, key=counts.get)

