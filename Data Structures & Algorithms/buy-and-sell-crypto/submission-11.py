class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        if(len(prices) == 1):
            return 0
        

        profit = prices[right] - prices[left]


        while ( right < len(prices)):

            if (prices[left] > prices[right]):
                left = right

            

            if(profit < prices[right] - prices[left]):
                profit = prices[right] - prices[left]
            


            right+=1
        

        if (profit <=0):
            return 0

        else:
            return profit


        