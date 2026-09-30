class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #locating a duplicate value in an array 

        #input [1,2,2]

        #output: 2 since theres 2 2s in the array

        #im thinking we iterate and build a dictionary and then return the key with a value greater than 1

        #how could this be O(1) of extra space not instant access i misread that ? 


        dic ={}

        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        
        return max(dic, key=dic.get)
        