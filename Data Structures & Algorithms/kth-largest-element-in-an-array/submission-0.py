class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        count = 0 
            # pop heap k-1 times 
        while(count < k-1):
            heapq.heappop(nums)
            count +=1


        ans = heapq.heappop(nums)
        return -ans
        