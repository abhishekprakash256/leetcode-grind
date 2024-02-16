"""
make the maximum profit from selling the stocks 
"""

prices = [7,1,5,3,6,4]
out = 5

prices2 =  [7,6,4,3,1]
out2 = 0 




"""
algo --- 

order is imp


#base case 
if len(nums) == 0 or len(nums) == 1:
    return 0 

#initilize the vars

l = 0 
r = l + 1

max_val = nums[l]
min_val = nums[r]

while r < len(nums):

    #check the condn

    if  nums[l] < min_val:

        min_val = min(min_val,nums[l])
    
    if nums[r] > max_val:

        max_val = max(max_val,nums[r])

    l +=1
    r +=1



return nums[r] - nums[l]

"""