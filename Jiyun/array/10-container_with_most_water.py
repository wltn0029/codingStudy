class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # First trial (Time Limit Exceeded Error)

        maxWater = float("-inf")
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                maxWater = max(maxWater, (j - i) * min(height[i], height[j]))
                
        return maxWater

    # -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Time Complexity: O(n)
        
        water = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            water = max(water, (r - l) * min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return water