#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'

# def solve(S: str) -> str:
def solve(S):
    slist = [0 for x in range(26)]
    sdict = dict(zip("abcdefghijklmnopqrstuvwxyz", [x for x in range(26)]))
    for s in S:
        #slist[sdict[s]] += 1
        index = sdict.get(s)
        if index != None:
            slist[index] += 1

    slist = [x for x in slist if x !=0]
    slist = sorted(slist)

    clist = [0 for x in range(101)]
    for s in slist:
        clist[s] += 1

    r = "Yes"
    for c in clist:
        if c !=0 and c != 2:
            r = "No"
            break
    return r
    #pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)
    print(a)

def main2():
    with open("./abc349/abc349_b/test/sample-3.in") as f:
        S = f.read()
    a = solve(S)
    print(a)

    with open("./abc349/abc349_b/test/sample-3.out") as f:
        b = f.read()
    print(b)

def main3():
    import generate
    S = generate.main()

    a = solve(S)
    print(a)

if __name__ == '__main__':
    #main()
    main2()
    #main3()
