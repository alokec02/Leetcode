class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        R = len(robot)
        F = len(factory)
        INF = 10 ** 20

        def get_min(rindex, findex):
            if rindex == R:
                return 0
            if findex == F:
                return INF

            x, limit = factory[findex]

            best = get_min(rindex, findex + 1)

            for i in range(1, limit + 1):
                if rindex + i > R:
                    break
                cost = 0
                for j in range(rindex, rindex + i):
                    cost += abs(x - robot[j])
                best = min(best, get_min(rindex + i, findex + 1) + cost)
            
            return best
        
        return get_min(0,0)

        