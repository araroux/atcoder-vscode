#!/usr/bin/env python3
# from typing import *

# def solve(N: int, T: int, A: List[int]) -> int:
def solve(N, T, A):
    A = [a-1 for a in A]

    tt = [[] for i in range(N)]
    yy = [[] for i in range(N)]
    nn = [[],[]]

    flg = 0
    for k, a in enumerate(A):
        i = a // N
        j = a % N
        yy[i].append(a)
        if len(yy[i]) == N:
            flg = 1
            break
        tt[j].append(a)
        if len(tt[j]) == N:
            flg = 1
            break

        if i == j:
            nn[0].append(a)
            if len(nn[0]) == N:
                flg = 1
                break
        if (N-1-i) == j:
            nn[1].append(a)
            if len(nn[1]) == N:
                flg = 1
                break

    if flg == 1:
        if k+1 <= T:
            print(k+1)
        else:
            print(-1)
    else:
        print(-1)
    return

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main2():
    with open("./abc355/abc355_c/test/sample-2.in") as f:
        a = f.read().split("\n")
    N,T = list(map(int, a[0].split()))
    A = list(map(int, a[1].split()))
    a = solve(N, T, A)
    #print(a)

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    T = int(next(tokens))
    A = [None for _ in range(T)]
    for i in range(T):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, T, A)
    #print(a)

if __name__ == '__main__':
    main()
