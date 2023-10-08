class Solution:
    def isanagram(self, s:str, t:str):
       return sorted(s) == sorted(t)
    
s1=Solution()

s = "car"
t = "rat"

res=s1.isanagram(s,t)
print (res)

s= "bat"
t= "atb"

res=s1.isanagram(s,t)
print(res)