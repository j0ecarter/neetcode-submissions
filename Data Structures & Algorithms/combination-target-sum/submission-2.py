class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or not target:
            return []

        res = []
        nums.sort()
        running_count = 0

        def backtracking(i, cur, running_count):
            if running_count == target:
                res.append(cur.copy())
                return res
            
            for val in range(i, len(nums)):
                new_total = running_count + nums[val]
                if new_total > target:
                    break
                cur.append(nums[val])
                backtracking(val, cur, new_total)
                cur.pop()

        backtracking(0, [], 0)
        return res