class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i for i in range(1,n+1)]

        print(circle)

        index = 0
        while len(circle) > 1:

            index = (index + (k-1)) % len(circle)

            circle.pop(index)

            # index now automatically points to next friend
            if index == len(circle):
                index = 0

        return circle[index]
