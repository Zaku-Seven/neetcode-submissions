class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        prefix =[1] * len(nums)
        suffix = [1] * len(nums)

        sumVal =0

        for i in range(1,len(nums)):
            sumVal = nums[i-1] * prefix[i-1]

            prefix[i] = (sumVal)

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(len(prefix)):

            output.append(prefix[i] * suffix[i])

        
        return output
            
            

        