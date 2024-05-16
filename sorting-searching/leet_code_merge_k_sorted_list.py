"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""

#test case 

lst = []
out = []


lst2 = [[]]
out = []



#modify the addition logic to the list

"""
algo --

two pointer 

cobine two 

jump into the third one and combine 

the leghth varis 

loops neede - 
	one for the iterration of the main list 
	one for the iteration of the secondry list
	

#base cases
if len(lst) == 0 
	return []

if len(lst) == 1
	return lst


new_lst = []

for i in range(len(lst) - 2 ):
	l = lst[i][0]
	r = lst[i+1][0]

	l,r = 0,0 
	while l < len(lst[i]):
		if lst[i][l] < lst[i][r]:

			new_lst.append(lst[i][l])
			l +=1

		elif lst[i][l] == lst[i][r]:

			new_lst.append(lst[i])
			new_lst.append(lst[l])
			i +=1
			l +=1

		else:
			new_lst.append(lst[l])
			l +=1




""" 
