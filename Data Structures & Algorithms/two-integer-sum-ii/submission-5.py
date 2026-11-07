class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            remaining = target - num

            if remaining in seen:
                return [seen[remaining], i + 1]
            
            seen[num] = i + 1
        
        return []
        