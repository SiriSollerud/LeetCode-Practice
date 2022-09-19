class Solution(object):
    def isPalindrome(self, s):

        if len(s) == 1:
            return True
        
        s = s.lower().replace(" ", "")
        
        for letter in s:
            if not letter.isalnum():
                s = s.replace(letter, "")
        
        if len(s) == 0:
            return True

        count_unique = 0
        for i in range(len(s)):
            if not s[i] == s[-i - 1]:
                count_unique += 1
                if count_unique > 1:
                    return False
        return True
        