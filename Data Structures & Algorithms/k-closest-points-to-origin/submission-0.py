from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        '''
        (sqrt((x1 - x2)^2 + (y1 - y2)^2))

        x2 = 0 

        y2 =0 

        i wanna push tuples to the heap and just return the second part in the tuple 


        '''

        heap = [] 

        heapq.heapify(heap)

        for point in points:

            heapq.heappush(heap, ((sqrt((point[0] - 0)**2 + (point[1] - 0)**2)), point))

        
        print(heap)
        ans = []
        while k !=0:
        
            dis, pair = heapq.heappop(heap)
            ans.append(pair)
            k -=1

        return ans
