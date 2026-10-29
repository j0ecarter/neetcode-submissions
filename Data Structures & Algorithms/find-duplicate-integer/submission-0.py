from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        countList = Counter(nums)
        
        for (num, count) in countList.items():
            if count > 1:
                return num