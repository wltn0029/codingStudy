class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        # First trial (Wrong answer: only consider sum of positive integers)

        tempA = format(a, "b")
        tempB = format(b, "b")
        
        if len(tempA) > len(tempB):
            tempB = "0"* (len(tempA) - len(tempB)) + tempB
        if len(tempA) < len(tempB):
            tempA = "0"* (len(tempB) - len(tempA)) + tempA
            # print(tempA, tempB)
        
        temp = ""
        C = 0
        for i in range(len(tempA)-1, -1, -1):
            # print(tempA[i], tempB[i])
            if tempA[i] == "1" and tempB[i] == "1":
                temp = str(C) + temp
                C = 1
                # print("x", temp)
                continue
            if C == 0:
                temp = str(int(tempA[i]) or int(tempB[i])) + temp
                # print("y", temp)
                continue
            
            if C:
                if tempA[i] == "0" and tempB[i] == "0":
                    temp = str(C) + temp
                    C = 0
                else:
                    temp = "0" + temp 
                # print("z", temp)
                continue
        if C:
            temp = "1" + temp 
        # print(temp)
            
        return int(temp, 2)
        
    # -----------------------------------------------------------------
        # Second trial refer to other's solution
        # Runtime: faster than 96.19%
        # Memory Usage: less than 34.66%
        
        MAX = 0x7FF
        MIN = 0x800
        mask = 0xFFF  # for negative value
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        if a >= MAX:
            return ~ (a ^ mask)
        return a


        # To understand the negative (from discussion)
        '''
        let us say a = -3, b = 1, mask=0xFF (0...11111111)

        binary python representation:
        a = 1...11111101
        b - 0...00000001

        a ^ b = 1...11111100
        a ^ b & mask = 0...11111100
        a & b = 0...00000001
        a & b << 1 = 0...00000010
        a & b << 1 & mask = 0...00000010

        so now
        a = 0...11111100
        b = 0...00000010

        a ^ b & mask = 0...11111110
        a & b << 1 & mask = 0...00000000

        a = 0...1111110 = 254
        b = 0...00000000 = 0

        max = 0x7F = 01111111 = 127

        a <= max: false

        a ^ mask = 0...00000001
        ~ (a ^ mask) = 1...11111110 = -2
        '''