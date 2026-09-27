class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_val = nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                min_val = min(min_val, nums[left])
                break

            min_val = min(min_val, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            # need to figure out some way of altering l, r depending on which side

        return min_val
                
