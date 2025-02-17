"""
Given two non-negative integers num1 and num2 represented as strings,
 return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the
inputs 
"""

"""
Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

"""

"""
approach -- 

mapper = {"0" : 0 , "1" : 1 , "2": 2 , "3" : 3 , "4": 4 , "5" : 5 , "6" : 6 , "7" : 7 , "8": 8 , "9": 9}

and make the numbers 

100 + 20 + 3 = 123
400 + 50 + 6 = 456




"""