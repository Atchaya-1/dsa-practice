from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
         # time O(n) - n*k(26), Space - O(n*k)
        d = defaultdict(list) # by default create a list if not exists on append list
        for s in strs:
            count = [0]*26
            for t in s:
                count[ord(t)-97] +=1
            key = tuple(count) # list mutable, can't be a key. need to convert it to tuple
            d[key].append(s)
        return d.values()

        # time - O(n * k log k), space - O(n)
        # group = defaultdict(list)
        # for s in strs:
        #     group[tuple(sorted(s))].append(s)
        # return list(group.values())



        """output = []    # time O(n2), Space - O(n2) - worst case
        seen = []
        for i,s in enumerate(strs):
            l = [s]
            for j,t in enumerate(strs):
              if i!=j and self.isanagram(s,t):
                l.append(t)
            output.append(l)
        for o in output:
            if sorted(o) not in seen:
               seen.append(sorted(o))
        return seen
            
          
    def isanagram(self,s1,s2):
        al = [0]*26
        for i,c in enumerate(s1):
            al[ord(c)-97] +=1
        for i,c in enumerate(s2):
            al[ord(c)-97] -=1
        for i in al:
            if i!=0:
               return False
        return True"""


    
strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
print(obj.groupAnagrams(strs))




# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
