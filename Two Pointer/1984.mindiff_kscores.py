class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l,r=0,k-1
        res=float("inf")

        while r < len(nums):
            res=min(res, nums[r]-nums[l])
            l+=1
            r+=1
        return res

s=Solution()
result=s.minimumDifference([9,4,1,7],2)
print(result)