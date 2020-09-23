#-*- encoding:utf -*-
# c problem https://codeforces.com/contest/879/problem/C
# 使用 ^ | & 顺序
import sys
 
all_zero = 0
all_one = (1 << 10) - 1
all_one = 1023
 
n = int(sys.stdin.readline().strip())
for line_idx in range(n):
    cmd_line_vec = sys.stdin.readline().strip().split(' ')
    oper = cmd_line_vec[0]
    const_num = int(cmd_line_vec[1])
    if oper == '&':
        all_zero = all_zero & const_num
        all_one = all_one & const_num
    elif oper == '|':
        all_zero = all_zero | const_num
        all_one = all_one | const_num
    elif oper == '^':
        all_zero = all_zero ^ const_num
        all_one = all_one ^ const_num
const_res_xor = const_res_and = const_res_or = 0
for idx in range(10):
    all_zero_this = all_zero >> idx
    all_one_this = all_one >> idx
    
    all_zero_thispos = all_zero_this & 1
    all_one_thispos = all_one_this & 1
    
    # ^ | &
    # 0 => 0 and 1 => 0
    if all_zero_thispos == 0 and all_one_thispos == 0:
        # ^ 0
        # | 0
        # & 0
        pass
    # 0 => 0 and 1 => 1
    elif all_zero_thispos == 0 and all_one_thispos == 1:
        # ^ 0
        # | 0
        # & 1
        const_res_and = const_res_and + (1 << idx)
    elif all_zero_thispos == 1 and all_one_thispos == 0:
        # ^ 1
        # | 0
        # & 1
        const_res_xor = const_res_xor + (1 << idx)
        const_res_and = const_res_and + (1 << idx)
    elif all_zero_thispos == 1 and all_one_thispos == 1:
        # ^ 0
        # | 1
        # & 1
        const_res_or = const_res_or + (1 << idx)
        const_res_and = const_res_and + (1 << idx)
 
print 3
print '^' + ' ' + str(const_res_xor)
print '|' + ' ' + str(const_res_or)
print '&' + ' ' + str(const_res_and)
