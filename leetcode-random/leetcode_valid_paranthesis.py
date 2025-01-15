class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 1:
            return False

        stack = []
        i = 0 

        mapper = {"(" : ")" , "{" : "}" , "[" : "]"}

        if s[0] == ")" or s[0] == "}" or s[0] == "]" :

            return False

        while i < len(s) :

            if s[i] in mapper:

                stack.append(s[i])
            
            else :

                if not stack :

                    return False

                para = stack.pop()

                if s[i] != mapper[para] :

                    return False
            i += 1

        if stack:

            return False

        return True
                    



        