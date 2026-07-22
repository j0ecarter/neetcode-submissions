class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive = []
        sorted_num = sorted(set(nums))
        if not sorted_num:
            return 0
        longest = 1
        current = 1

        for i in range(1, len(sorted_num)):
            if sorted_num[i] - sorted_num[i - 1] == 1:
                current += 1
            else:
                current = 1

            if current > longest:
                longest = current

        return longest
