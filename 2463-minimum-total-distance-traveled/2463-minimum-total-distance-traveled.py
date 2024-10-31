class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        R = len(robot)
        F = len(factory)
        INF = 10 ** 20
        
        @cache
        # rindex -> 0 to R
        # findex -> 0 to F
        # each input takes O(R^2)
        # O(R^3 * F) time
        def get_min(rindex, findex):
            if rindex == R:
                return 0
            
            if findex == F:
                return INF
                
            x, limit = factory[findex]
            
            # no take (take no robots)
            best = get_min(rindex, findex + 1)
            cost = 0
            
            # take i robots
            for i in range(1, limit + 1):
                if rindex + i > R:
                    break

                cost += abs(x - robot[rindex + i - 1])
                best = min(best, get_min(rindex + i, findex + 1) + cost)
            
            return best
            
        return get_min(0, 0)

        