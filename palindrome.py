class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newstr = ""
        # for i in s:
        #     if i.isalnum():
        #         newstr +=i.lower()
        # if newstr == newstr[::-1]:
        #        return True
        # return False

        
        i,l = 0,len(s)-1
        while i <= l: 
            if not self.isalnum(s[i]):
                i +=1   
            if not self.isalnum(s[l]):
                l -=1
                
            if s[i].lower() == s[l].lower():
                i +=1
                l -=1
            else:
               return False
        return True   
    def isalnum(self,c):
             return (ord('A') <= ord(c) and ord('Z') >= ord(c)) or (ord('a') <= ord(c) and ord('z') >= ord(c)) or (ord('0') <= ord(c) and ord('9') >= ord(c))  


input = "Was it a car or a cat I saw"
obj = Solution()
print(obj.isPalindrome(input))
        
