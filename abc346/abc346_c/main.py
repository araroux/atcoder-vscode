#!/usr/bin/env python3
# from typing import *

# def solve(N: int, K: int, A: List[int]) -> int:
def solve(N, K, A):
    bb = []
    for a in A:
        if a <= K:
            bb.append(a) # Kより小さな値のみ残す
    cc = set(bb) # Aの重複を削除
    ss = sum(cc) # Aの和を算出

    tt = (K*(K+1))//2 # 1からKまでの和を算出 大きな数で誤差が出るため必ず // 整数の商 にする
    return tt-ss

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    #with open("./abc346/abc346_c/test/sample-3.in") as f: tokens = iter(f.read().split())
    
    N = int(next(tokens))
    K = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, K, A)
    print(a)

if __name__ == '__main__':
    main()