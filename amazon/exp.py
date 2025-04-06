"""
Make the susbsets with two approaches 

"""



nums = [1,2,3]

def subsets(i, path):
    
    if i == len(nums):
        
        print(path)
        
        return None

    subsets(i + 1, path + [nums[i]])  # Include nums[i]
    subsets(i + 1, path)              # Exclude nums[i]


subsets(0, [])  # start from index 0 with empty subset




def backtrack(start, path):

	print(path)

	for i in range(start , len(nums)) :

		path.append(nums[i])

		backtrack(i+1,path)

		path.pop()



backtrack(0,[])

