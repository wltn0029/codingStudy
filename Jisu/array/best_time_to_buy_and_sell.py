class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        left = 0
        right = 1
        if len(prices) <= 1 : return 0
        while right < len(prices) :
            diff = prices[right] - prices[left]
            if diff <= 0:
                left = right
            else :
                if diff > max :
                    max = diff
            right += 1
        return max