#!/usr/bin/env python3
# from typing import *

# def solve(N: int, K: int, A: List[int]) -> Any:
def solve(N, K, A):
    pass  # TODO: edit here

    bb = []
    for a in A:
        if a % K == 0:
            bb.append(int(a/K))
    bb2 = sorted(bb)
    c = ""
    for b in bb2:
        c = c + "%d " % b
    #print(c[:-1])
    return c[:-1]

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    #tokens = iter(sys.stdin.read().split())
    #with open("./abc347_a/test/sample-1.in") as f:
    #    tokens = iter(f.read().split())
    with open("./abc347/abc347_a/test/sample-1.in") as f:
        tokens = iter(f.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, K, A)
    print(ans)  # TODO: edit here

if __name__ == '__main__':
    main()