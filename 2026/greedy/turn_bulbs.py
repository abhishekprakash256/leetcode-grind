"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.
"""

"""
approach -- 

test cases -- 

[1,0,1]
[0,1,0] - when flip the second one 


[1,0,1]
[1,1,0] - when flip the first one 

[1,0,1]
[1,0,0] - when flip the third one 



if == 1 : 

	continue

else flip 
cost += 1 




another case -- 

[0,0,0,1]
[1,1,1,0]

[0,0,0,1]
[0,1,1,0]


[0,1,1,1,0] -- fail




"""