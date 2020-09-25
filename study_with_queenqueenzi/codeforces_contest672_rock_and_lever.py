#-* encoding:utf8 -*-
#https://codeforces.com/contest/1420/problem/B
#只有两个数最高位都是1的时候才能&>=^，0 0或者0 1都不行
#因此转化为判断有几组二进制位数相等的问题
import sys
import math
t = int(sys.stdin.readline().strip())
for idx_t in range(t):
    n = int(sys.stdin.readline().strip())
    a_vec = sys.stdin.readline().strip().split(' ')

    #位数
    a_bits_dict = dict()
    for this_a in a_vec:
        a_bits = int(math.log2(int(this_a)))
        if a_bits in a_bits_dict:
            a_bits_dict[a_bits] += 1
        else:
            a_bits_dict[a_bits] = 1
    this_res = 0
    for k, v in a_bits_dict.items():
        this_res = this_res + int(v * (v - 1) / 2)
    print(this_res)

