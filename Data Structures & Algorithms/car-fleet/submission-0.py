class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        pairs.sort(reverse=True)

        time_taken = (target - pairs[0][0]) / pairs[0][1]
        num_of_group = 1

        for i in range(1, len(pairs)):
            car = pairs[i]
            car_time = (target - car[0]) / car[1]

            if car_time > time_taken:
                num_of_group += 1
                time_taken = car_time
        return num_of_group
        