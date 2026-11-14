class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l, r = 0, 1
        res = [nums[0]]

        while r < len(nums):
            if nums[l] != nums[r]:
                res.append(nums[r])
                l = r
            r += 1

        nums[:] = res
        return len(res)