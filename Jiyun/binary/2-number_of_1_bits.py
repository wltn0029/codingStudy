class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # First trial
        # Runtime: faster than 13.85%
        # Memory Usage: less than 88.22%

        ham = 0
        for _n in str(format(n,"b")):
            if _n == "1":
                ham += 1
        
        return ham

    # -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Runtime: faster than 52.01%
        # Memory Usage: less than 36.86%

        return bin(n).count("1")
    
    # -----------------------------------------------------------------
        # Third trial refer to other's solution
        # Runtime: faster than 90.53%
        # Memory Usage: less than 36.86%

        ham = 0
        while n:
            n = n & (n - 1)
            ham += 1
        return ham
    
    