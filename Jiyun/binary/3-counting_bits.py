class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        # First trial
        # Time Complexity: O(n) /   Runtime: faster than 35.20%
        # Space Complexity: O(n) /   Memory Usage: less than 98.47%

        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        n -= 1
        
        ans = [0, 1]
        temp = [1, 2]
        count = 0
        while n:
            ans.append(temp[count])
            count += 1
            if count == len(temp):
                temp = temp[:] + [x + 1 for x in temp]
                count = 0
            n -= 1
        return ans


    # -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Time Complexity: O(n) /   Runtime: faster than 48.73%
        # Space Complexity: O(n) /   Memory Usage: less than 31.89%

        ans = [0]
        for i in range(1, n+1):
            ans.append(ans[i << 1] + i % 2)
        return ans