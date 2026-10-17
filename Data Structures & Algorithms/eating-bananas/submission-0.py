import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] - number of banannas in pile
        # h - number of hours you have to eat all of the bannanas
        # k - bannanas per hour eating rate
        # if piles[i] < k - cannot eat more than those ones
        # k needs to be the minimum value
        # h >= len(piles)
        left, right = 1, max(piles)
        final_val = 0

        while left <= right:
            mid = (left + right) // 2
            time = 0

            for val in piles:
                time += math.ceil(val / mid)
            if time <= h:
                final_val = mid
                right = mid - 1
            else:
                left = mid + 1
        return final_val

