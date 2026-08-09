class Solution:
    
    def isAnagram(self, s: str,t: str):
        char = [0]*26
        for i in s:
            char[ord(i)- 97] +=1
        for j in t:
            char[ord(j)- 97] -=1

        for c in char:
            if c!=0:
               return False
            
        return True

  
obj = Solution()
print(obj.isAnagram("cat","ac"))