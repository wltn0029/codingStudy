class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# [Wrong Answer] in [-3,4,3,90] 0   
#         nums_index = [[x, i] for i,x in enumerate(nums)]
#         new_nums = filter(lambda x: x[0] <= target, nums_index)
        
#         for i in range(len(new_nums) - 1):
#             for j in range(i + 1, len(new_nums)):
#                 # print(i, new_nums[i], j, new_nums[j])
#                 # print(new_nums[i] + new_nums[j])
#                 if new_nums[i][0] + new_nums[j][0] == target:
#                     return [new_nums[i][1], new_nums[j][1]]


# First trial (O(n^2))

#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# Second trial refer to other's solution (O(n))
        seen = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in seen:
                return(seen[m], i)
            else:
                seen[n] = i
                