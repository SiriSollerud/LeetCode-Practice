class Solution(object):
    def isSubsequence(self, s, t):
        
        # input: subsequence (s: str), full_string (t: s)
        # output: if subsequence is in full_string (bool)
        #         --> can't disturb the position 
        #         --> Input: s = "abc", t = "ahbgdc"
        #             Output: true
        
        seq = ""
        for letter in s:
            if letter in t:
                letter_t_index = t.index(letter)
                t = t[letter_t_index + 1:]
            else:
                return False
        return True