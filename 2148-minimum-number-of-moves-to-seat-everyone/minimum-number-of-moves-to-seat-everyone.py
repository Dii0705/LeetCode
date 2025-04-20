class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Greedy
        # Time Complexity: nlog(n)
        seats.sort()
        students.sort()
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i]-students[i])
        return moves