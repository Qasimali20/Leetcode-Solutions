class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right= 0, len(s)-1
        
        while left < right :
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[left].lower() != s[right].lower():
                 return False
            else:
                left+=1
                right-=1
        return True

solution=Solution()

s1 = "A man, a plan, a canal: Panama"
s2="race a car"

result=solution.isPalindrome(s1)
result1=solution.isPalindrome(s2)

print(result)
print(result1)