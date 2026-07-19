# Time: O(n) - single loop through array
# Space: O(n) - set stores up to n elements
# Trade-off: using extra memory (set) to avoid O(n²) nested loops

class Solution:
    
    def two_sum(self, num: list,target: int) ->list:
       
        data = {}
        for i,x in enumerate(num):
            y = target - x # 5-1 = 4,5-2=3,5-3=2
            if y in data:
                return data[y],i
            data[x] = i

        """for i in range(len(num)):  # Time: O(n^2) - nested loop
            for j in range(len(num)): # Space: O(1) - only i, j used, no extra storage
                if i!=j and num[i]+num[j]==target:
                    return i,j 
        """
        

       
num = [1,6,3]
target = 7
  
obj = Solution()
print(obj.two_sum(num,target))
