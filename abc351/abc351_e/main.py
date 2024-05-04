#!/usr/bin/env python3
# from typing import *

# def solve(N: int, X: List[int], Y: List[int]) -> int:
#def solve(N, X, Y):
def solve(XY_):

    #import time
    #start1 = time.perf_counter() #計測開始

    XY0 = []
    XY1 = []
    for x, y in XY_:
        if (x%2==0 and y%2==0) or (x%2==1 and y%2==1):
            XY0.append([x,y])
    for x, y in XY_:
        if (x%2==0 and y%2==1) or (x%2==1 and y%2==0):
            XY1.append([x,y])

    #start2 = time.perf_counter() #計測終了
    #print('{:.5f} ms'.format((start2-start1)*1000))

    ret = 0
    length = len(XY0)
    for i in range(length-1):
    #for i in range(1,2):
        for j in range(i+1,length):
            xi,yi = XY0[i] 
            xj,yj = XY0[j]
            xixj = abs(xi-xj)
            yiyj = abs(yi-yj)
            a = xixj if xixj > yiyj else yiyj
            ret += a
    length = len(XY1)
    for i in range(length-1):
    #for i in range(1,2):
        for j in range(i+1,length):
            xi,yi = XY1[i] 
            xj,yj = XY1[j]
            xixj = abs(xi-xj)
            yiyj = abs(yi-yj)
            a = xixj if xixj > yiyj else yiyj
            ret += a

    #start3 = time.perf_counter() #計測終了
    #print('{:.5f} ms'.format((start3-start2)*1000))

    return ret

def main():
    N = int(input())
    #X = [None for _ in range(N)]
    #Y = [None for _ in range(N)]
    XY = []
    for i in range(N):
        #X[i], Y[i] = map(int, input().split())
        XY.append(list(map(int, input().split())))
 
    #a = solve(N, X, Y)
    a = solve(XY)
    print(a)

def main2():
    XY = []
    with open("./abc351/abc351_e/test/sample-2.in") as f:
        a = f.read().split()
        N = int(a[0])
        b = a[1:]
        for i in range(N):
            XY.append([int(b[2*i]), int(b[2*i+1])])
    a = solve(XY)
    print(a)

def main3():
    import generate
    XY = []
    a = generate.gen()
    N = int(a[0])
    b = a[1:]
    for i in range(N):
        XY.append([int(b[2*i]), int(b[2*i+1])])
    a = solve(XY)
    print(a)

if __name__ == '__main__':
    main()
