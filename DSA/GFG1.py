'''
PS: Given a set of coordinates points of the form [p, q] and a line L of the form ax + by + c = 0.
The task is to find a point on a given line for which the sum of distances from a given set of coordinates is minimum.
'''

from typing import List

def getPerpendicularPoint(params: List[int],point: List[int]) -> List[float]:
    points = list([])
    constCC = float(point[1])-params[0]*float(point[0])
    x = (constCC - params[2])/(params[1] - params[0])
    y = params[1]*x + params[2]
    points.append(x)
    points.append(y)
    return points

dist = lambda p1,p2: (((float(p1[0])-p2[0])**2) + ((float(p1[1])-p2[1])**2))**0.5

class Solution:
    def findOptimumCost(self, line : List[int], points : List[List[int]]) -> float:
        res = 1e6
        slopeP = float(line[1])/float(line[0])
        constC = float(line[2])/float(line[1])*(-1.0)
        slopeN = float(line[0])/float(line[1])*(-1.0)

        for p in points:
            ds = 1e6
            try:
                td = 0
                pt = getPerpendicularPoint([slopeP,slopeN,constC],point = p)
                for x in points:
                    td += dist(x,pt)
                if ds > td:
                    ds = td
            except Exception as exc:
                print(exc)
                pass
            if res > ds:
                res = ds
        return res

obj = Solution()
res1 = obj.findOptimumCost([2,1,4],[[-1,2],[1,3],[2,4]])
res2 = obj.findOptimumCost([1,-1,-3],[[-3,-2],[-1,0],[-1,2],[1,2],[3,4]])
print("{0:.2f}".format(res1))
print("{0:.2f}".format(res2))