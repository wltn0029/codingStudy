class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # First trial (poor performance)
        # Time Complexity: O(n*n) /   Runtime: faster than 16.05%
        # Space Complexity: O(n) /   Memory Usage: less than 48.31%

        result = []
        nums.sort() # refer to other's solution
        
        for i in range(len(nums)-1):
            target = 0 - nums[i]
            seen = {}
            for j in range(i + 1, len(nums)):
                n = nums[j]
                temp = target - n
                if temp in seen:
                    if [nums[i], temp, n] not in result:
                        result.append([nums[i], temp, n])
                else:
                    seen[n] = n
                    
        return result

    # -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Time Complexity: O(n*n) /   Runtime: faster than 77.42%
        # Space Complexity: O(n) /   Memory Usage: less than 48.31%
        
        result = []
        nums.sort()
        
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    mid += 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]:
                            mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                            right -= 1
                    mid += 1
                    right -= 1
        
        return result