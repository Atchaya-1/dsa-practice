class Solution:
    
    def reverse(self, s: list) ->list:
        
        # Time - O(n), Space - O(n)
        # stack = [] 
        # while s:
        #     stack.append(s.pop())
        # return stack

        l,r = 0,len(s) - 1

        # Time - O(n), Space - O(1)
        # for i in range(r):
        #     s[i],s[r] = s[r],s[i]
        #     r -=1
        # return s

        # Time - O(n), Space - O(1) recursion
        def rev(l,r):
           
            if l < r: # 0 < 4
                s[l],s[r] = s[r],s[l]
                l +=1
                r -=1
                rev(l,r)
            return s
        return rev(l,r)
       

input = ["h","e","l","a","b"]
obj = Solution()
print(obj.reverse(input))
        

