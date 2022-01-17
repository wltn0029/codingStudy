class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # First trial (with division T.T)

        # answer = []
        # total = 1
        # isZero = False
        # zeroCount = 0
        
        # for num in nums:
        #     if num == 0:
        #         isZero = True
        #         zeroCount += 1
        #         if zeroCount >= 2:
        #             return [0]*len(nums)
        #         continue
        #     total *= num
        
        # for num in nums:
        #     if (num == 0):
        #         answer.append(total)
        #     else:
        #         if isZero:
        #             answer.append(0)
        #             continue
        #         answer.append(total/num)
        
        # return answer

    # -------------------------------------------------
        # Second trial refer to other's solution

        # n = len(nums)
        # left = [1] * n
        # right = [1] * n
        # answer = [0] * n
        
        # for i in range(n-1):
        #     left[i+1] = nums[i] * left[i]
        # for i in range(n-1, 0, -1):
        #     right[i-1] = nums[i] * right[i]
        # for i in range(n):
        #     answer[i] = left[i] * right[i]
        # # print(left, right, right_test)
        # return answer

    # -------------------------------------------------
        # Third trial (faster than second)

        # n = len(nums)
        # left = [1] * n
        # right = [1] * n
        # answer = [0] * n
        
        # for i in range(n-1):
        #     left[i+1] = nums[i] * left[i]
        #     right[n-2-i] = nums[n-1-i] * right[n-1-i]
        # for i in range(n):
        #     answer[i] = left[i] * right[i]
        # # print(left, right)
        # return answer

    # -------------------------------------------------
        # Forth trial (less memory)

        # n = len(nums)
        # answer = [1] * n

        # temp = 1
        # for i in range(n):
        #     answer[i] = temp
        #     temp *= nums[i]

        # temp = 1
        # for i in range(n-1, -1, -1):
        #     answer[i] = answer[i] * temp
        #     temp *= nums[i]

        # return answer

# -------------------------------------------------
        # Fifth trial (fastest)
        
        ans = [1]*len(nums)
        pi = pj = 1
        
        for i in range(len(nums)):
            j = -1-i
            
            ans[i] *= pi
            ans[j] *= pj
            pi *= nums[i]
            pj *= nums[j]
        
        return ans