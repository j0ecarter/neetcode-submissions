class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for (index, num) in enumerate(nums):
            remaining = target - num
            if remaining in values:
                return [values[remaining], index]
            values[num] = index