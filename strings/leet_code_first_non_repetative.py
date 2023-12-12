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


class Solution:
    def firstUniqChar(self, s: str) -> int:

        #the double loop solution
        
        for i in range(0,len(s)-1):
            count = 0

            for j in range(i+1,len(s)-1):

                if s[i] == s[j]:
                    count +=1
                
            if count == 0 :
                return i 
        
        return -1 


if __name__ == "__main__":
    sol = Solution()
    res = sol.firstUniqChar(s3)

    print(res)
        
        