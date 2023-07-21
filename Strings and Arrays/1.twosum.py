class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        #{0:7}
        for i,n in enumerate(nums):
            if n in dict:
                return dict[n],i
            else:
                dict[target-n]=i

# Create an instance of the Solution class
solution = Solution()

# Test case 1
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Expected output: [0, 1]

# Test case 2
nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print(result)  # Expected output: [1, 2]

# Test case 3
nums = [3, 5, 2 ,1]
target = 3
result = solution.twoSum(nums, target)
print(result)  # Expected output: [0, 1]
