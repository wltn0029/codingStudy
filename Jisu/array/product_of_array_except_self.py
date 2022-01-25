class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [nums[0]]
        back = [nums[-1]]
        for i in range(1, len(nums)):
            front.append(front[-1]*nums[i])
        for i in range(2, len(nums)+1):
            back.append(back[-1]*nums[len(nums) - i])
        
        ans = []
        print(front)
        print(back)
        for i in range(0, len(nums)):
            if i == 0 :
                ans.append(back[len(nums) -2])
            elif i == len(nums) -1 :
                ans.append(front[i-1])
            else :
                ans.append(front[i-1]*back[len(nums)-i-2])
            
        return ans