class Solution:
    def search(self, nums, target) -> int:
        
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
           
            
            if nums[m] ==target:
                return m

            if target > nums[m] or (target < nums[m] and nums[l] > target  ): 
               
                l = m+1
            else:
                r = m-1
                print(nums[l],nums[r],nums[m])
         
        return -1

obj = Solution()
nums = [4,5,6,7,0,1,2]
print(obj.search(nums,2))

