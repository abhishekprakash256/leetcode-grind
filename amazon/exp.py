"""
Make the susbsets with two approaches 

"""



def subsets(i, path):
    if i == len(nums):
        print(path)
        return
    subsets(i + 1, path + [nums[i]])  # Include nums[i]
    subsets(i + 1, path)              # Exclude nums[i]


print(subsets(2,[1,2]))

