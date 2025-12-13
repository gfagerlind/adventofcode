import sys
from itertools import combinations
import collections

with open(sys.argv[1]) as f:
    points = [tuple(map(int, l.split(","))) for l in f.read().split("\n") if l]
    print(
        max(
            (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            for ((x1, y1), (x2, y2)) in combinations(points, 2)
        )
    )
    def is_allowed(x1,y1, x2,y2):
        # need to figure out the stupid order
        x_l = min(x1,x2)
        x_r = max(x1,x2)
        y_u = min(y1,y2)
        y_d = max(y1,y2)
        #order = []
        if len([(x,y) for x,y in points if x_l < x < x_r and y_u < y < y_d]):
            return False
        mid_x = 0.5 + (x_r + x_l)/2
        mid_y = 0.5 + (y_d + y_u)/2
        crossed_points = 0
        for i, (x_a,y_a) in enumerate(points):
            if i == len(points)-1:
                x_b, y_b = points[0]
            else:
                x_b, y_b = points[i+1]
            x_m = min(x_a, x_b)
            x_M = max(x_a, x_b)
            y_m = min(y_a, y_b)
            y_M = max(y_a, y_b)
            if x_m < mid_x < x_M and 0 < y_b < mid_y:
                crossed_points += 1
            if x_a == x_b and x_l < x_a < x_r and y_m < mid_y < y_M:
                return False
            if y_a == y_b and y_u < y_a < y_d and x_m < mid_x < x_M:
                return False
        if crossed_points % 2 == 1:
            return True
        return False
    res = {
        (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1): f"{x1},{y1},{x2},{y2}"
        for ((x1, y1), (x2, y2)) in combinations(points, 2)
        if is_allowed(x1,y1,x2,y2)
    }
    print(m:=max(res))
