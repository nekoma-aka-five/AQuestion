# -*- using utf8 -*-
#https://atcoder.jp/contests/abc179/tasks/abc179_e
#求和时利用循环
import sys
inputlinevec = sys.stdin.readline().strip().split(' ')
n = int(inputlinevec[0])
x = int(inputlinevec[1])
m = int(inputlinevec[2])
 
sum_res = x
crcle_dict = dict()
crcle_list = list()
crcle_idx = 0
pre_a = x
 
for idx in range(1, n):
    #a范围在0-m之间，不会无限递增，因此很大概率会重复
    #a * a % m这种单变量的式子，一旦a出现了之前出现过的值
    #后续就会出现重复的序列，然后循环
    this_a = (pre_a * pre_a) % m
    pre_a = this_a
    
    if this_a not in crcle_dict:
        crcle_dict[this_a] = 1
        crcle_list.append(this_a)
        sum_res = sum_res + this_a
    else:
        crcle_step = len(crcle_list) - crcle_list.index(this_a)
        remain_crcle = int((n - idx) / crcle_step)
        remain_crcle_tail = int((n - idx) % crcle_step)
        
        crcle_sum = 0
        crcle_sum_tail = 0
        for a_item in crcle_list[crcle_list.index(this_a):]:
            crcle_sum = crcle_sum + a_item
            remain_crcle_tail = remain_crcle_tail - 1
            if remain_crcle_tail == 0:
                crcle_sum_tail = crcle_sum
        sum_res = sum_res + (remain_crcle * crcle_sum) + crcle_sum_tail
        break
    
print(sum_res)
