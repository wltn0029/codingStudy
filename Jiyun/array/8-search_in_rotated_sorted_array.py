class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # First trial (Wrong answer: 159/195 tests passed)

        left = 0
        right = len(nums) - 1
        
        if left == right:
            if nums[left] == target:
                return left
        
        while left < right:
            mid = (left + right) // 2
            # print(mid, left, right)
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[mid] == target:
                return mid
            
            mid_val = (nums[left] + nums[right] + 1) / 2
            # print(mid_val)
            
            if mid_val >= target:
                left = mid + 1
            else:
                right = mid
            
        return -1

# -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Time Complexity: O(log n)

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1