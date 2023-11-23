class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # check if the list is of length 1, return 0 if so
        
        # create a max, buy, and scout value
        maxP, buy, scout = 0, 0, 1
        
        #use while loop to iterate the scout while less than price length
        while scout < len(prices):
            
            # check if we need to update buy if the scout is less than the buy
            if prices[scout] < prices[buy]:
                buy = scout
                
            # check if need to update max value; update if value of scout - buy > maxP
            if prices[scout] - prices[buy] > maxP:
                maxP = prices[scout] - prices[buy]
                
            # increment scout
            scout += 1
            
        #return max value
        return maxP
            
        
            
        