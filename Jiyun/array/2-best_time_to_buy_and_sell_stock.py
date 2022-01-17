class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # First trial (Time Limit Exceeded)
        
        # maxProfit = 0
        
        # for i in range(len(prices)-1):
        #     for j in range(i + 1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j] - prices[i])
        # return max(maxProfit, 0)

                
    # -------------------------------------------------
        # Second trial refer to other's solution

        maxProfit, minPrice = 0, float("inf")
        for price in prices:
            minPrice = min(price, minPrice)
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)
            
        return maxProfit