class Solution(object):
    def isSubsequence(self, s, t):
        for letter in s:
            if letter in t:
                letter_t_index = t.index(letter)
                t = t[letter_t_index + 1:]
            else:
                return False
        return True