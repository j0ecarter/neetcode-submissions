class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        postfix = []
        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
            # prefix.append(nums[i] * nums[i+1])
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output