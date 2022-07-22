def minCostClimbingStairs(self, cost: List[int]) -> int:
        # o(n2)
        # going to use recusion

        res = [None]

        def recStep(cost, step, spent):

            if step > len(cost):
                return res

            if step == len(cost):
               
                if res[0] == None:
                    res[0] = spent
                    return res
            
                elif spent < res[0]:
                    
                    res[0] = spent
                    return res
                
                return res

            # now we go two steps or one
            
            recStep(cost, step + 1, spent + cost[step])
           # else:
           #     recStep(cost, step + 1, spent + 0)
            if step + 2 <= len(cost):
                    
                recStep(cost, step + 2, spent + cost[step])
                
        recStep(cost, 0 , 0)
        recStep(cost, 1 , 0)
       
        return res[0]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            cost.append(0)

            for i in range(len(cost) - 3, -1, -1):
                cost[i] += min(cost[i + 1], cost[i + 2])

            return min(cost[0], cost[1])


