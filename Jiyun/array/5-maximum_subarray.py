class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # First trial (Time Limit Exceeded error)
        
        # max_sum = float("-inf")
        # sub_sum = 0
        
        # for i in range(len(nums)):
        #     sub_sum = nums[i]
        #     max_sum = max(sub_sum, max_sum)
        #     for j in range(i+1, len(nums)):
        #         sub_sum += nums[j]
        #         max_sum = max(sub_sum, max_sum)
                
        # return max_sum

# -----------------------------------------------------------------
        # Second trial (Wrong Answer)

        # max_sum = float("-inf")
        # sub_sum = 0
        # arr = [0] * len(nums)
        
        # for i in range(len(nums)):
        #     sub_sum += nums[i]
        #     max_sum = max(sub_sum, max_sum)
        #     arr[i] = sub_sum
        
        # print(arr, max_sum)
        # # max_sum = max(arr)
        # if len(nums) == 1:    
        #     return max_sum
    
        # sub_sum = max_sum
        
        # for i in range(len(nums)):
        #     sub_sum -= nums[i]
        #     # print(sub_sum)
        #     max_sum = max(sub_sum, max_sum)
                
        # return max_sum

# -----------------------------------------------------------------
        # From third trial, 
        # https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
# -----------------------------------------------------------------
        # Third trial refer to other's solution (DP memoization)
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # !Issue @cache makes undefined error

        # @cache
        @functools.cache
        def solve(i, must_pick):
            if i >= len(nums): 
                return 0 if must_pick else float("-inf")
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)

# -----------------------------------------------------------------
        # Forth trial refer to other's solution (DP tabulation)
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        # dp = nums[:]
        # # print(dp)
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i], nums[i] + dp[i-1])
        # # print(dp)
        # return max(dp)

# -----------------------------------------------------------------
        # Fifth trial refer to other's solution (Kadane's Algoirthm)
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # curMax = nums[0]
        # maxTemp = nums[0]

        # for i in range(1, len(nums)):
        #     curMax = max(nums[i], nums[i] + curMax)
        #     maxTemp = max(maxTemp, curMax)
        # return maxTemp
            