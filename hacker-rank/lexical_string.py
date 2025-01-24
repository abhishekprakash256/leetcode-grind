"""
when dealing with strings. A string is greater than another string if it comes later in a 
lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters.
 This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition
Example

The next largest word is .

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

Function Description

Complete the biggerIsGreater function in the editor below.

biggerIsGreater has the following parameter(s):

string w: a word
Returns
- string: the smallest lexicographically higher string possible or no answer

Input Format

The first line of input contains , the number of test cases.
Each of the next  lines contains .

Constraints

 will contain only letters in the range ascii[a..z].
Sample Input 0

5
ab
bb
hefg
dhck
dkhc
Sample Output 0

ba
no answer
hegf
dhkc
hcdk

"""

"""
approach -- 

put in a list 

sort the list 

put in reverse orrder 

make the string 
result = ""

start from the back 

and match the heirachy 

[h,g,f,e] -> [e,f,g,h]

hefg -> hegf



"""

result = []

def helper_dfs(temp_lst,s) :
	"""
	The function to make the result list 
	"""

	#base case

	#if length is equal 
	if len(temp_lst) == len(s) :

		result.append(temp_lst)

		return

	#make the recursive call
	for j in range(len(s)) :

		helper_dfs(temp_lst + s[j] , s)


def biggerIsGreater_slow(s):
	"""
	The fucntion to make bigger string 
	"""

	#constraints case 
	if len(s) == 1:

		return s

	#vars
	i = 0 
	temp_str = ""

	#make the recursive call
	helper_dfs(temp_str,s)

	result.sort()

	for i in range(len(result)):

		if result[i] == s :

			break

	print(result)

	if i < len(result)  :

		return result[i+1]


	return "no answer"


	
#-------------------------------------------------------------------------------------------------------------








