class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash = {}
        arr = []
        for i in nums:
            hash[i] = hash.get(i,0)+1

        


        for j in range(k):
            max_key = max(hash, key=hash.get)
            arr.append(max_key)
            hash.pop(max_key)

        return arr

        