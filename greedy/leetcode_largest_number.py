"""
Given a list of non-negative integers nums, arrange them such that 
they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

"""

"""
Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109


"""


"""
approach -- 

sort the array 

[2,10]

make str and attach 

210 

doesn't work in all the cases 

in single and double digits 

nums = [3,30,34,5,9]

split all the digits and sort the values 

and add the values

split the values

new_nums = []

for number in numbers :
	string_number = str(number)
    digits = [int(char) for char in string_number]
    digit_list.append(digits)


"""

class Solution:
	"""
	Passes leetcode
	"""
    def largestNumber(self, nums: List[int]) -> str:
        # Convert integers to strings
        array = list(map(str, nums))
        
        # Custom sorting with a lambda function
        array.sort(key=lambda x: x*10, reverse=True)
        
        # Handle the case where the largest number is "0"
        if array[0] == "0":
            return "0"
        
        # Build the largest number from the sorted array
        largest = ''.join(array)
        
        return largest