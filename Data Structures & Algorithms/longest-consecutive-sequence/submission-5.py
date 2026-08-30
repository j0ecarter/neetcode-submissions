class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        newNums = set(nums)

        for num in nums:
            if (num - 1) not in newNums:
                length = 0
                while (num + length) in newNums:
                    length += 1
                    if length > longest:
                        longest = length
            else:
                pass
                
        return longest
