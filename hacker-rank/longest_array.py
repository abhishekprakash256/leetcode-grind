"""

Given an array of integers, find the longest subarray where the absolute
difference between any two elements is less than or equal to 1.
"""

"""

approach - sort the elment 

use two pointer l , r start from 0 and len(nums) -1 

then find the diff in the first and the last element

[1,1,1,1,1,2,2,3,3]


[1,1,2,2,4,4,5,5,5]

sliding window approach ? 

start two pointer l ,r 

keep sliding right and store the max length


#constarints case 
if len(nums) == 0 :

    return 0 

if len(nums) == 1:
    
    return 1 


"""

def pickingNumbers(a):
    """
    code passes
    """
    # Write your code here

    #constraints case 
    if len(a) == 0 :

        return 0

    if len(a) == 1 :

        return 1

    #sort the array
    a.sort()

    #make the ptrs 
    l , r = 0 , 1

    max_length = 0

    while r <= len(a) - 1 :

        if abs(a[l] - a[r]) <= 1 :

            r += 1

        else :
            
            l = r
            r += 1

        #get the max length
        max_length = max( (r-l) , max_length )


    return max_length


print(pickingNumbers([1,1,1,1,1]))

