class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)) :
            finding = target - nums[i]
            if seen.get(finding) != None :
                return [i, seen.get(finding)]
            else :
                seen[nums[i]] = i
        