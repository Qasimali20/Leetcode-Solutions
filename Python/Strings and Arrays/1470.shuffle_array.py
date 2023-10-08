class Solution:
    def shuffle_array(self,nums):
        n=len(nums)//2
        res=[]
        for i in range (n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
    
s1=Solution()

nums=[2,3,6,8,1,4]
x=s1.shuffle_array(nums)
print(x)