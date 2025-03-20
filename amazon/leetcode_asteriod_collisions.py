"""
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction 
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
 both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


"""


"""
Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0


"""

"""

approach -- 


if abs(num[i]) > abs(nums[i+1]) :

    res = nums[i]

elif abs(nums[i]) == abs(nums[i]) :

    res = nums[i]

using a stack

positive value append 

negtaive value pop and do calc 


"""


class Solution_wrong:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        The function to find the asteriod that remains 
        """

        #make the stack
        stack = [asteroids[0]]

        #start the stack iter 
        for i in range(1,len(asteroids)) :

            if asteroids[i] > 0 :

                stack.append(asteroids[i])


            else :

                curr_astr = asteroids[i]

                while curr_astr < 0 :

                    prev_astr = stack.pop()

                    #do the calc 
                    if abs(prev_astr) > abs(curr_astr) :

                        stack.append(prev_astr)

                        curr_astr = prev_astr


        return stack[0]



                        

"""



Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""


"""
approach -- 

[10,2,-5]

make a stack

when see positve append 

when see negative pop the element 

and do the calculation 

curr_asteriod = asterios[i]

if curr_asteriod < 0 :

    while stack or stack[-1] < 0 :

        prev_asteriod = stack.pop()

        #calc 

        if abs(prev_asteriod) > abs(curr_asteriod) :

            stack.append(prev_asteriod)

        else:

            stack.append(curr_asteroid)



"""




class Solution:
    """
    passes leetcode
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Function to find the asteroids that remain after all collisions
        """

        # Stack to hold surviving asteroids
        stack = []

        # Loop over the list of asteroids
        for asteroid in asteroids:
            # Handle the case where the asteroid is moving right
            while stack and asteroid < 0 and stack[-1] > 0:
                # There is a collision
                top = stack[-1]
                
                # If the current asteroid is larger, pop the stack and continue checking
                if top < -asteroid:
                    stack.pop()
                    continue
                # If both asteroids are of the same size, pop the stack and do not add the new asteroid
                elif top == -asteroid:
                    stack.pop()
                    break
                # If the current asteroid is smaller, break (it is destroyed)
                else:
                    break
            else:
                # If no collision or it's a right-moving asteroid, simply add to the stack
                stack.append(asteroid)

        return stack


















        







































