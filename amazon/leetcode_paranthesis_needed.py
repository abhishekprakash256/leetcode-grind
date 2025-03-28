"""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
"""


"""

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""


"""
approach -- 

using a stack 

and count the len of stack 

(())) -> stacks get's empty need to return the length remain

((() -> stack works 

)))) -> stack doesn't work

((( -> 

return len(stack) 

"((((())"


"""
class Solution:
    """
    passes leetcode
    """
    def minAddToMakeValid(self, s: str) -> int:
        """
        The function to find the number of paranthesis needed
        """

        #constarint case 
        if len(s) == 1 :

            return 1 

        open_para = 0
        close_para = 0

        for para in s :

            if para == "(" :

                open_para += 1 

            elif para == ")" and open_para >= 1  :

                open_para -= 1

            else :

                close_para +=1


        return open_para + close_para 








