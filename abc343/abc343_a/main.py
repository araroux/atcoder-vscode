#!/usr/bin/env python3
# from typing import *

# def solve(A: int, B: int) -> int: 
def solve(A, B):
    #pass  # TODO: edit here
    for i in range(10):
        if i != A+B: break
    return i

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    #with open("./abc343/abc343_a/test/sample-2.in") as f:
    #    A, B = map(int, f.read().split())        
    #with open("./abc349/abc349_a/test/sample-2.in") as f:
    #    A, B = map(int, f.read().split())        
    A, B = map(int, input().split())

    a = solve(A, B)
    print(a)

if __name__ == '__main__':
    main()