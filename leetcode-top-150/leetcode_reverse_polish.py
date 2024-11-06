"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

"""


"""
tokens = ["2","1","+","3","*"]

Output: 9
Explanation: ((2 + 1) * 3) = 9



tokens = ["4","13","5","/","+"]

Explanation: (4 + (13 / 5)) = 6

out = 6 


Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""


"""

second / first 
second - first 



["4","13","5","/","+"]

stack = []

operators = ("+", "-" , "/" , "*" )


for i in range(len(tokens)) : 

    if tokens[i] not in operators:
        
        stack.append(tokens[i])

    
    elif tokens[i] == "+" :
        
        first = tokens.pop()
        second = toekens.pop()
        val = first + second 
        tokens.append(val)
    
    
    elif tokens[i] == "*" :
        
        first = tokens.pop()
        second = toekens.pop()
        val = first * second 
        tokens.append(val)
    
    elif tokens[i] == "-" :
        
        first = tokens.pop()
        second = toekens.pop()
        val = second - first
        tokens.append(val)
    
    elif tokens[i] == "/" :
        
        first = tokens.pop()
        second = toekens.pop()
        val = second / first
        tokens.append(val)   


"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        The function to find the reverse polish notion
        passes leet code 
        """

        stack = []

        operators = ("+", "-" , "/" , "*" )


        for i in range(len(tokens)) : 

            if tokens[i] not in operators:
                
                stack.append(int(tokens[i]))

            
            elif tokens[i] == "+" :
                
                first = stack.pop()
                second = stack.pop()
                val = first + second 
                stack.append(val)
            
            
            elif tokens[i] == "*" :
                
                first = stack.pop()
                second = stack.pop()
                val = first * second 
                stack.append(val)
            
            elif tokens[i] == "-" :
                
                first = stack.pop()
                second = stack.pop()
                val = second - first
                stack.append(val)
            
            elif tokens[i] == "/" :
                
                first = stack.pop()
                second = stack.pop()
                val = int(second / first)
                stack.append(val)

        return stack[-1]     

        