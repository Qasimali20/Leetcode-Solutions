class Solution:
    def contains_duplicate(self,nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                 return True
            
            return False

s1=Solution()

nums = [1, 2, 3, 1]
result = s1.contains_duplicate(nums)
print(result)  

nums = [1, 2, 3, 4]
result = s1.contains_duplicate(nums)
print(result)  # Expected output: False

# Test case 3
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result = s1.contains_duplicate(nums)
print(result) 