class Solution:
    def isValid(self, s: str) -> bool:

        paran = {"{" : "}","[" : "]","(" : ")"}
    
        stack = []

        for i,c in enumerate(s):
            if c not in paran:
                if stack and c==paran[stack[-1]]:
                  stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack)==0
        


        # failed when s = "[" and l resets each time it get valid paranthesis
        # c = list(s)
        # while l < len(c):

        #     if c[l] not in paran:
        #         if c[l] == paran[c[l-1]]:
        #             c.remove(c[l])
        #             c.remove(c[l-1])
        #             l=0
        #         else:
        #             return False
        #     else:
        #         l +=1
        # if len(c)==0:
        #     return True
        # return False

obj = Solution()
s = "[]()()"
print(obj.isValid(s))