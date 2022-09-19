class Solution(object):
    def isPalindrome(self, s):
        
        # return true if palindrome
        #   convert to lowercase
        #   remove all non-alphanumeric chars
        #   alpha-numeric = letters and numbers

        if len(s) == 1:
            return True
        
        s = s.replace(" ", "")
        s = s.lower()
        for letter in s:
            if not letter.isalnum():
                s = s.replace(letter, "")
        if len(s) == 0:
            return True

        check = False
        count_unique = 0
        for i in range(len(s)):
            if s[i] == s[-i - 1]:
                check = True
            else:
                count_unique += 1
                check = False
                
        if check and count_unique <= 1:
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """
        