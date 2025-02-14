"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


"""
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


"""


"""
approach -- 

using a stack LIFO

make a mapper

mapper = { ")" : "(" , "]" : "[" , "}" : "{" }

pop and get the element and match


{}

"){"
"""

class Solution:
    """
    passes leetcode
    """
    def isValid(self, s: str) -> bool:
        """
        The function to check if it's a valid parenthesis
        """

        #dict
        mapper = { ")" : "(" , "]" : "[" , "}" : "{" }

        #constraint case 
        if len(s) == 1 :

            return False

        stack = []

        for para in s :

            if para not in mapper :

                stack.append(para)

            else:

                if stack:

                    temp_para = stack.pop()

                    if mapper[para] != temp_para :

                        return False
                else:

                    return False
                    
        if stack :

            return False

        return True


