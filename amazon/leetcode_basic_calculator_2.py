"""
Given a string s which represents an expression, evaluate this expression and return its 
value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as 
mathematical expressions, such as eval().
"""


"""

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
"""


"""
approach using a stack ? 

pop when see the sign ? 

BODMAS

how to keep the prioriy use the if conditons ? 

DMAS

start reding from right to left 

append in array as see the number and pop 

store the result and calculate 

"""


class Solution:
    """
    wrong solution 
    """
    def calculate(self, s: str) -> int:
        """
        The function to do the calculation
        """

        #constaint case 
        if len(s) == 1 :

            return int(s)


        #make the stack 
        stack = []

        #ptrs
        r = len(s) - 1 

        #opertor set
        operator = ("*","/","-","+") 


        while r >= 0 :

            print(s[r])

            if s[r] not in operator :

                stack.append(int(s[r]))

            elif s[r] == "/" :

                val = stack.pop()

                res = int(s[r-1]) / val

                stack.append(int(res))

            elif s[r] == "*" :

                val = stack.pop()

                res = int(s[r-1]) * val
                stack.append(int(res))

            elif s[r] == "+" :

                val = stack.pop()

                res = int(s[r-1]) + val 

                stack.append(int(res))


            elif s[r] == "-" :

                val = stack.pop()

                res = int(s[r-1]) - val

            
                stack.append(int(res))

            r -= 1

        return res





s = "3+2*2"


sol = Solution()

print(sol.calculate(s))


