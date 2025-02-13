"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

	I can be placed before V (5) and X (10) to make 4 and 9. 
	X can be placed before L (50) and C (100) to make 40 and 90. 
	C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""

"""
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').



"""

"""

brute force approach  -- 


mapper = {"I":1, "IV" :4 , "IX" = 9, "X" : 10 , "XL" : 40 , "L" : 50, "XC": 90 , "C": 100 , "CD": 400, "LD": 450 , XD":490 , "CM": 900 , "LM": 950 , "XM": 990 , "M":1000}


total = 0 

MCMXCIV

M - 1000
CM - 900
XC - 90
IV - 4

i,j 

45
XLV


take one pointer 

check value add 

check the prev value and update if less 














"""



class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        passes leetcode
        """
        
        # Correct Roman numeral mapping
        mapper = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        # Base case: if the input is empty, return 0
        if not s:
            return 0

        # Vars
        num = 0
        length = len(s)

        # Loop through the string
        for i in range(length):
            # If the current numeral is smaller than the next, subtract it (for cases like IV = 4, IX = 9)
            if i < length - 1 and mapper[s[i]] < mapper[s[i + 1]]:
                num -= mapper[s[i]]
            else:
                num += mapper[s[i]]
        
        return num

		

sol = Solution()

print(sol.romanToInt("MCMXCIV"))



			



