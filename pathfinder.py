from fract import get_fraction

def calculate_path(pointA, pointB):
    go = lambda a : int(a/abs(a))
    path = [pointA]
    # Direct approach (to be optimized)
    steps = [pointB[0]-pointA[0], pointB[1]-pointA[1]]
    print(steps[1]/steps[0])
    slope = get_fraction(steps[1]/steps[0])
    print(slope[0]/slope[1])
    slope
    while steps[0] != 0 or steps[1] != 0:
        l = path[-1]
        for _ in range(slope[0]):
            if steps[0]:
                path.append([l[0]+go(steps[0]), l[1]])    
                steps = [pointB[0]-path[-1][0], pointB[1]-path[-1][1]]
                l = path[-1]
            else:
                break
        for _ in range(slope[1]):
            if steps[1]:
                path.append([l[0], l[1]+go(steps[1])])
                steps = [pointB[0]-path[-1][0], pointB[1]-path[-1][1]]
            else:
                break
    return path