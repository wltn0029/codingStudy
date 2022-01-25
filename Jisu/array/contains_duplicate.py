class Solution:
    def mergeSort(self, array: List[int]) ->List[int] :
        # split
        if len(array) <= 1 : return array
        half = len(array)//2
        left = array[:half]
        right = array[half:]
        
        #merge sort
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        
        #merge
        leftIdx = 0
        rightIdx = 0
        sorted = []
        while leftIdx < len(left) and rightIdx < len(right):
            leftNum = left[leftIdx]
            rightNum = right[rightIdx]
            if leftNum >= rightNum:
                sorted.append(leftNum)
                leftIdx += 1
            else:
                sorted.append(rightNum)
                rightIdx += 1
        
        while leftIdx < len(left) :
            sorted.append(left[leftIdx])
            leftIdx += 1
        
        while rightIdx < len(right) :
            sorted.append(right[rightIdx])
            rightIdx += 1
        
            
        return sorted
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted = self.mergeSort(nums)
        left = 0
        right = 1
        while right < len(nums):
            if sorted[left] == sorted[right] :
                return True
            left += 1
            right += 1
        return False