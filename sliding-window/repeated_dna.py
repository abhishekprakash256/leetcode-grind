"""
the repeated dna problem
"""

class Solution():
	def find_repeated_sequences(s, k):
	    """
	    the function to find the repeated sequences of given length 
	    """

	    #vars 
	    mapper = {}
	    left = 0 
	    right = k - 1 

	    #star the iter loop 
	    while right < len(s):

	        if s[left:right+1] not in mapper:
	            mapper[s[left:right + 1]] = 1
	        
	        else:
	            mapper[s[left:right + 1]] +=1
	        
	        left+=1
	        right+=1

	    return {key for key in mapper if mapper[key] > 1}
	    
	    #get the final results 
	    
	def find_repeated_sequences_optim(s, k):
	    """
	    The hash set code 
	    """

	    seen,res = set(),set()

	    for i in range(len(s)-k):

	        subs = s[i:i+k]

	        if subs in seen:
	            res.add(subs)

	        seen.add(subs)

	    return list(res)
	 







