#coding=utf-8
import sys
import math

def maxSubArray(a):
    ans = a[0]
    n = len(a)
    pre, cnt = -9999999999, -9999999999

    for i in range(n):
        if i != 0:
            cnt = max(pre + a[i], a[i]);
            pre = cnt;
        else:
            pre = a[0];
        ans = max(ans, cnt);
    return ans;


if __name__ == "__main__":

    input = str(sys.stdin.readline().strip())
    values = []
    values.append(list(map(int, input.split(','))))

    sum = maxSubArray(values[0])

    print(sum)