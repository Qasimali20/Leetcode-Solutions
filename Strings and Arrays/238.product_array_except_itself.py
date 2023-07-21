class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[1]* (len(nums))

        prefix=1
        postfix=1

        for i in range (len(nums)):
            res[i]=prefix
            prefix *= nums[i]

        for i in range (len(nums)-1, -1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res

s=Solution()

nums1=[1,2,3,4]
num2=[-1,1,0,-3,3]

res1=s.productExceptSelf(nums1)
res2=s.productExceptSelf(num2)

print(res1)
print(res2)