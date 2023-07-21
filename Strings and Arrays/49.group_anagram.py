from collections import defaultdict

class solution:
    def groupanagram(self, strs: list[str]):
        res=defaultdict(list)

        for word in strs:
            sorted_word=''.join(sorted(word)) 
            # firstly the words are sorted and then join method is usd for the concatenation of string

            res[sorted_word].append(word)
            #now after sorting if sorted word has a key it will add the
            #orignal word to that list(append method)...if sorted word has no key then a new key will be created with an empty list

        return list(res.values())
    
s1=solution()
# Test the groupanagram method
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result=s1.groupanagram(strs)

print(result)

