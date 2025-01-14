"""
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
"""


"""
Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV
 

Constraints:

1 <= num <= 3999

"""


"""
approach -- 

I	1
V	5
X	10
L	50
C	100
D	500
M	1000

{ 1:I, 2 : II , 3 : III , 4 : IV , 5: V , 6: VI , 7:VII ,8: VIII, 9: IX, 10 : X, 40: XL , 50 :L , 90 : XC , 100 : C, 200 : CC, 300 : CCC , 600 : DC , 700 : DCC , 800 , 2000 : MM , 3000 : MMM ,450 : LD,500:D, 900:CD ,950 :LD,1000 : M }


103 = 100 + 3 

99 : 
90 + 9 

103 = 100 + 3 

3999 = 3000 + 900 + 90 + 9 

1000 + 1000 + 1000 + 900 + 90 + 9 

390 = 300 + 90 


390 // 100 = 3 

390 % 100 = 90 

"""


class Solution():

	def intToRoman(self,num):
		"""
		The function to make the int to Roman 
		pass leet code
		"""
		mapper = {0 : "" ,1: "I", 2 : "II" , 3 : "III" , 4 : "IV" , 5: "V" , 6: "VI" , 7: "VII" ,8: "VIII", 9: "IX", 10 : "X", 20 : "XX" , 30 : "XXX", 40: "XL" , 50 :"L" , 60 : "LX" , 70: "LXX", 80 : "LXXX", 90 : "XC" , 100 : "C", 200 : "CC", 300 : "CCC" , 400 : "CD" , 600 : "DC" , 700 : "DCC" , 800 :"DCCC" , 2000 : "MM" , 3000 : "MMM" ,450 : "LD",500:"D", 900:"CM" , 950 :"LD",1000 : "M" }


		#initilaize the empty string
		roman_number = ""

		#divide and get remainder 
		thousand = num // 1000 
		rem = num % 1000 

		roman_number += mapper[thousand*1000]

		hundred = rem // 100
		rem = rem % 100

		roman_number += mapper[hundred*100]

		tenth = rem // 10 
		rem = rem % 10

		roman_number += mapper[tenth*10]

		ones = rem

		roman_number += mapper[ones]

		return roman_number



sol = Solution()

print(sol.intToRoman(3749))

