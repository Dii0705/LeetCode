class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Reverse the sorted array, because the arrival time is capped by the previous car speed
        cars = sorted(zip(position,speed), reverse = True)
        # for pos,s in cars:
        #     time = (target - cars[pos]) / cars[s]
        times = [(target-p)/s for p,s in cars] 
        fleets = 0
        t0 = 0

        for t in times:
            if t > t0:
                fleets +=1
                t0 = t
        return fleets