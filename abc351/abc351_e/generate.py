#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def gen():
    #N = random.randint(1, 1000)  # TODO: edit here
    N = 100000

    X = [None for _ in range(N)]
    Y = [None for _ in range(N)]
    for i in range(N):
        X[i] = random.randint(1, 10 ** 8)  # TODO: edit here
        Y[i] = random.randint(1, 10 ** 8)  # TODO: edit here

    a = []
    print(N)
    a.append(N)
    for i in range(N):
        #print(X[i], Y[i])
        a.append(X[i])
        a.append(Y[i])
    return(a)

if __name__ == "__main__":
    gen()
