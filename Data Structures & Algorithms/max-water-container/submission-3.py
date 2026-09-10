class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_area = 0
        i, j = 0, len(heights) - 1

        while i < j:
            left = heights[i]
            right = heights[j]
            height = min(left, right)
            largest_area = max(largest_area, (height * (j-i)))

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return largest_area
