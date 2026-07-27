# Two Sum II - sorted array
# Uses two-pointer instead of hashmap since array is already sorted
# Time: O(n), Space: O(1) - better than hashmap version's O(n) space

class Solution:
    
    def two_sum(self, num: list,target: int) ->list:

      i,l = 0,len(num)-1

      while i < l:
         
        if num[i]+num[l] == target:
           return i+1,l+1
        if num[i]+num[l] > target:
           l -=1
        else:
           i +=1
        

       
num = [1,2,3,4,5]
target = 9
  
obj = Solution()
print(obj.two_sum(num,target))
