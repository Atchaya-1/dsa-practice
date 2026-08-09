class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substr = set()
        maxl = 0
        left =0 
        for i,a in enumerate(s):
            while s[i] in substr:
                substr.remove(s[left])
                left +=1
            substr.add(s[i])
            maxl = max(len(substr),maxl)
        return maxl
    
s = "abba"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
