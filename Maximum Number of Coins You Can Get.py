class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()  # O(nlogn)
        coins = 0

        i = len(piles) //3
        while i < len(piles):
            coins += piles[i]
            i += 2

        return coins
