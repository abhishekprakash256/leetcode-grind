"""
Given a set of distinct integers, print the size of a maximal subset of  where the sum of any  
numbers in  is not evenly divisible by k.
"""



"""
approach -- 

s = [1,7,2,4]
k = 3 

two subsets 

1 + 7 = 8 -
1 + 2 = 3
1 + 4 = 5 -
7 + 2 = 9 
7 + 4 = 11 -
2 + 4 = 6

1 + 7 = 8 
1 + 4  = 5
7 + 4 = 11

subset = [1,7,4]

making all possible two subsets and not divible by k 

then make a list of the subset list 

go through all value and add in the main list and give the length back
"""


#maket the result list 
result = []
final_lst = []

#debug the code

def helper_dfs(i,temp_lst,k,s):
	"""
	The helper dfs for making the two pairs that is not divisible
	"""
	#base case

	#the length is equal 
	if len(temp_lst) == 2 and sum(temp_lst) % k != 0:

		result.append(temp_lst)

		return

	#make the recursive call
	for j in range(i,len(s)):

		if s[j] not in temp_lst:

			helper_dfs(j+1,temp_lst + [s[j]] ,k ,s)


def nonDivisibleSubset(k, s):
	"""
	The main function for recursive calls and find the pairs
	"""

	#constarints case 
	if len(s) == 0 or len(s) == 1  :

		return 0 

	#make the vars
	temp_lst = []
	i = 0

	#make the recursive calls
	helper_dfs(i,temp_lst,k,s)

	#make the final list
	for sequence in result :

		for num in sequence :

			if num not in final_lst :

				final_lst.append(num)

	print(result)

	#return the result
	return len(set(final_lst))






def nonDivisibleSubset(k, s):
    """
    Find the largest subset such that the sum of any two numbers is not divisible by k.
    """
    # Step 1: Count remainders when elements are divided by k
    #code passes

    remainder_count = [0] * k
    
    for num in s:
        remainder_count[num % k] += 1

    # Step 2: Include at most one element with remainder 0
    max_subset_size = min(remainder_count[0], 1)

    # Step 3: Process pairs of remainders
    for i in range(1, (k // 2) + 1):
        if i == k - i:  # Special case for the middle remainder
            max_subset_size += min(remainder_count[i], 1)
        else:
            max_subset_size += max(remainder_count[i], remainder_count[k - i])

    return max_subset_size





s = [1,7,2,4]
k = 3 

s2 = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436 ]
k2 = 7


print(nonDivisibleSubset(k2,s2))



