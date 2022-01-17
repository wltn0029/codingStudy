class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # First trial refer to other's solution
        # Time Complexity: O(log n)
        # Space Complexity: O(1)

        left = 0
        right = len(nums) - 1
        # print("----")
        while(left < right):
            mid = (left + right) // 2
            # print(mid, right, left)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
            # print(mid, right, left)
        
        return nums[right]