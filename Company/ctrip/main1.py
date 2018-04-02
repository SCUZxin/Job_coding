#!/bin/python
import sys
import os

# 用一个链表来表示从 A->B ，所有的全部指向完成

#A、B、C、D、E   N[5][5]

# 4
# A2B3D
# A4C2E
# A5D
# C3B

def char2Num(c):
    if c == "A": return 1
    elif c == "B": return 2
    elif c == "C": return 3
    elif c == "D": return 4
    elif c == "E": return 5

def calculate(M, strs):
    N = [[0 for i in range(6)] for i in range(6)]

    # 将距离装换成数组
    for i in range(1, len(strs)+1):
        str = strs[i-1]
        for j in range(0,len(str)):
            if (j+2) <= len(str):
                if str[j+1].isdigit():
                    N[char2Num(str[j])][char2Num(str[j+2])] = int(str[j+1])



    return N

# ******************************结束写代码******************************

_M = int(input())

_strs_cnt = _M
_strs_i = 0
_strs = []
while _strs_i < _strs_cnt:
    try:
        _strs_item = input()
    except:
        _strs_item = None
    _strs.append(_strs_item)
    _strs_i += 1

res = calculate(_M, _strs)

print(res)