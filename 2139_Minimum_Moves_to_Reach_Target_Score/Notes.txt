class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        if maxDoubles == 0:
            moves += target - 1
            return moves

        while target > 1 and maxDoubles > 0:
            if target % 2 != 0:
                target -= 1
                moves += 1
            target //= 2
            maxDoubles -= 1
            moves += 1
        
        if maxDoubles == 0:
            moves += target - 1

        return moves
    