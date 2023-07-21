class Solution:
    def restoreString(self, s, indices):
        n = len(s)
        shuffled = [''] * n

        for i in range(n):
            shuffled[indices[i]] = s[i]

        return ''.join(shuffled)


s1 = Solution()
s = "eodc"
indices = [3,1,2,0]

s = "lthamoirg"
indices = [3,0,8,5,7,6,1,2,4]
shuffled_string = s1.restoreString(s, indices)
print(shuffled_string)
