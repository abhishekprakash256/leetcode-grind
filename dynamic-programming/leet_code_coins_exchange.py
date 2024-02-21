"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

coins = [1,2,5]
amount = 11
out = 3 

coins2 = [2]
amount2 = 3
out2 = -1

coins3 = [1]
amount3 = 0 
out3 = 0 


"""
Algo -- 

[1,2,5]
11

5 + 5 + 1 = 11

make a tree for calculation of the change of the items 
till one gives zero 

if greater than the sum gives False out 

run DFS in graph to calculate the least height of the tree


if I do memoization then complexity can be saved 


Algo recursion brute force --- 

#vars 
sum_change = -0 

#base case 
if sum_change == amount:
    return True

elif sum_change > amount:
    return False


#constraints
if amount == 0 :
    return 0    

two functions -----


fun helper 




fun coinChange
    





"""