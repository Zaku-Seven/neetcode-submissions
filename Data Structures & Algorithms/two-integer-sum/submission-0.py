class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        adding distinct indices that equal our target

        always assume we have a matching pair, so edge isn't needed here

        approaches-

        two pointers 

        hashmap 
        key value pairs, look at keys that equal up to target 


        '''
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j and nums[i]+ nums[j] == target):
                    result.append(i)
                    result.append(j)
                    return result


                    
        
        