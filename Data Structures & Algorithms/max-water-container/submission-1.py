class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_area = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            area = (j-i) * min(heights[i], heights[j])

            if area > largest_area:
                largest_area = area
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return largest_area
