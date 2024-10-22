"""
Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.
"""

"""

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


"""



"""
explanation --

mapper = {
    1:"I", 5:"V", 10:"X", 50:"L",
    100:"C", 500:"D", 1000:"M"
}



mapper = {
    1:"I", 4 : "IV", 5:"V", 9 : "IX", 10:"X", 40: "XL" 50:"L", 90: "XC" , 100:"C", 400:"CD" ,500:"D", 900:"CM" , 1000:"M"}

100 

- break it in small like ones 
- tens
- hundreds 
- thousands 

3000

1994 

1000
900
90
4 

MCMXCIV

try to break in small and integers 


2494


1000 - M
1000 - M
400 -  CD
90 - XL
4 = IV

[1000,1000,400,90,4]

8 - 

5 
1 
1
1




2388 -

1000 - M
1000 - M
300
    - 100 - C
    - 100 - C
    - 100 - C
80
    - 50 - L 
    - 10 - X
    - 10 - X
    - 10 - X
8 
    - 5 - V
    - 3
        - 1 - I
        - 1 - I
        - 1 - I    



[1000,1000,100,100,100,50,10,10,10,5,1,1,1]


MMCCCLXXXVIII

2388- 

2000
    - 1000
    - 1000
300
    - 100
    - 100
    - 100
88
    - 50
    - 30
        - 10
        - 10
        - 10
    - 8
        - 5
        - 1
        - 1
        - 1




"""















