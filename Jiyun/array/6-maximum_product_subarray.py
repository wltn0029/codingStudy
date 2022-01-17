class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # First trial refer to other's solution
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        curMax, curMin = 1, 1
        maxval = nums[0]
        
        for num in nums:
            val = (num, curMax * num, curMin * num)
            curMax, curMin = max(val), min(val)
            # print(curMax, curMin)
            maxval = max(maxval, curMax)
        
        return maxval

# -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # Explanation
        # First, Consider there is no zero, and if we get the products of all the numbers:
        # 1) We will have a negative result if there are odd numbers of negative -> max ((product of (0, last negative)), (product of (first negative, last num))
        # 2) We will have a positive result if there are even numbers of negative -> product of all the numbers
        # If there is a zero, that means we would have two subproblems(unless the zero is at index 0 or last index), 
        # if two zeros, 3 subs, all the way up.
        # We still can calculate from the very beginning and end at the same time, then we would get the result.

        original = nums[:]
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            original[i] *= original[i-1] or 1
            reverse[i] *= reverse[i-1] or 1
        # print(original, reverse)
        return max(original + reverse)