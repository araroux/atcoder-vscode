#!/usr/bin/env python3
# from typing import *

MOD = 998244353

# def solve(a: int, b: int, c: List[int], d: List[int], e: List[int]) -> Any:
def solve(a, b, c, d, e):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a, b = map(int, input().split())
    c = [None for _ in range(b)]
    d = [None for _ in range(b)]
    e = [None for _ in range(b)]
    for i in range(b):
        c[i], d[i], e[i] = map(int, input().split())
    ans = solve(a, b, c, d, e)
    print(ans)  # TODO: edit here

if __name__ == '__main__':
    main()
