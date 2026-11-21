class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        condition = len(nums) // 2
        count = {}

        for num in nums:
            val = count.get(num, 0) + 1
            if val > condition:
                return num
            count[num] = val
            
        return 0
        