"""
A video player plays a game in which the character competes in a hurdle race. Hurdles are of 
varying heights, and the characters have a maximum height they can jump. There is a magic potion 
they can take that will increase their maximum jump height by  unit for each dose. How many doses 
of the potion must the character take to be able to jump all of the hurdles. If the character can
 already clear all of the hurdles, return 0.

Example
"""

def hurdleRace(k, height):
    # Write your code here
    #code passes
    
    max_jump = max(height) 
    
    if k > max_jump :
        
        return 0
    
    return max_jump - k 