class Solution:
    
    def has_duplicate(self, num: list) ->bool:
        return len(num) > len(set(num))  #Time: O(n) and Space: O(n)

        """for i,x in enumerate(num):
              for j,y in enumerate(num):  #Time: O(n^2) and Space: O(1)
                   if i!=j and x==y:
                        return True
        return False
        """
        """
        data = set()
        for i in num:
            if i in data:         #Time: O(n) and Space: O(n)
                return True
            data.add(i)
        return False
        """
            
num = [1,2,8,8]
obj = Solution()
print(obj.has_duplicate(num))