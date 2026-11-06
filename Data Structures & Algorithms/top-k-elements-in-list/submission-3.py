from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        rank_count = sorted(count, key=count.get, reverse=True)
        return rank_count[:k]
