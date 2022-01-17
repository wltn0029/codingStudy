class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # First trial

        # nums_dict = {}
        
        # for num in nums:
        #     if num in nums_dict:
        #         return True
        #     else:
        #         nums_dict[num] = 0
        
        # return False
    
    # -------------------------------------------------
        # Second trial (fastest)

        # print(set(nums), len(set(nums)))
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
        
    # -------------------------------------------------
        # Third trial refer to other's solution

        # return len(nums) > len(set(nums))