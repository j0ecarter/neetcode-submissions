class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:
            survive = True

            while res and res[-1] > 0 and asteroid < 0:
                if res[-1] < -asteroid:
                    res.pop()
                elif res[-1] == -asteroid:
                    res.pop()
                    survive = False
                    break
                else:
                    survive = False
                    break

            if survive:
                res.append(asteroid)

        return res