# Initally overcomplicated this problem a ton by assuming that 
# I had to reconstruct the palindrome as well as count it
# Note to self: REACTO!!
        

class Solution(object):
    def longestPalindrome(self, s):
        pairs = 0
        unique_letters = set()
        
        for letter in s:
            if letter in unique_letters:
                pairs += 1
                unique_letters.remove(letter)
            else:
                unique_letters.add(letter)
                
        if unique_letters:
            return pairs * 2 + 1
        else:
            return pairs * 2