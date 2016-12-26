__author__ = "jalfaizy"

# code for https://www.hackerrank.com/challenges/find-point

n = input()
for i in range(n):
    px, py, qx, qy = raw_input().strip().split()
    px, py, qx, qy = int(px), int(py), int(qx), int(qy)
    
    x = 2*qx - px
    y = 2*qy - py
    
    print x, y    
