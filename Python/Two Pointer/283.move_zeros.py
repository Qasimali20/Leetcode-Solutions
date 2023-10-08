class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        while (i<len(nums)):
            if nums[i]==0:
                nums.append(0)
                nums.remove(0)
            i+=1

s=Solution()

nums=[1,4,0,4,0,3,0,6]
s.moveZeroes(nums)
print(nums)