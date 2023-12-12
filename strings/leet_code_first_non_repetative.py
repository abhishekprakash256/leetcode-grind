"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""


#test case 

s = "leetcode"
out = 0 

s2 = "loveleetcode"
out2 = 2 

s3 = "aabb"
out3 = -1


#wrong solution 
class Solution:
    def firstUniqChar(self, s: str) -> int:

        #make hash map 
        mapper = {}
        
        for i in range(len(s)):
            count = 0

            # The inner loop should start from i + 1 to compare the current character (s[i]) 
            # with the rest of the characters in the string.
            for j in range(i + 1, len(s)):

                mapper[s[i]] = True

                if s[i] == s[j]:
                    count += 1
                
            if count == 0 and s[j] not in mapper:
                return i 
        
        return -1



if __name__ == "__main__":
    sol = Solution()
    res = sol.firstUniqChar(s)

    print(res)
        
        