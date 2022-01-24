class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # First trial
        # Time Complexity: O(n) /   Runtime: faster than 38.59%
        # Space Complexity: O(1) /   Memory Usage: less than 70.10%
        
        n = len(nums)
        return n*(n+1)/2 - sum(nums)

    # -----------------------------------------------------------------
        # Second trial refer to other's solution
        # XOR solution

        # Time Complexity: O(n) /   Runtime: faster than 40.23%
        # Space Complexity: O(1) /   Memory Usage: less than 70.10%

        res = len(nums)
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= i
        return res

        # HOW IT WORKS
        '''
        A number XOR itself will become 0, any number XOR with 0 will stay unchanged. 
        So if every number from 1...n XOR with itself except the missing number, the result will be the missing number.

        Example: 0 ~ 4 missing 3
        1^2  ^4 ^1^2^3^4
        => 0^0^3^0 => 3
        '''
