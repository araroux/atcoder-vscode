#!/usr/bin/env python3
# from typing import *

# def solve(N: int, A: List[int]) -> int:
def solve(N, A):
    #print(N)
    B = [A[0]]
    for a in A[1:]:
        B.append(a)
        while(1):
            if len(B) > 1 and B[-2] == B[-1]:
                #B = B[:-1]
                B.pop()
                B[-1] += 1
            else:
                break
    return(len(B))
    #pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A)
    print(a)

def main2():
    with open("./abc351/abc351_c/test/sample-2.in") as f:
        tokens = iter(f.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A)
    print(a)

if __name__ == '__main__':
    main2()
