import sys
n = int(sys.stdin.readline().strip())
m_a = [[0 for idx_i in range(n)] for idx_j in range(n)]
for idx_i in range(n):
    thislinevec = sys.stdin.readline().strip().split(' ')
    for idx_j in range(n):
        m_a[idx_i][idx_j] = int(thislinevec[idx_j])

full_s = 1 << n
m_dp = [[float('inf') for i in range(n)] for s in range(full_s)]
m_dp[0][0] = 0
m_dp[1][0] = 0

for s in range(full_s):
    for i in range(n):
        if s >> i & 1:
            pre_s = s ^ (1 << i)
            for otherpot_idx in range(n):
                if pre_s >> otherpot_idx & 1:
                    m_dp[s][i] = min(m_dp[s][i],m_dp[pre_s][otherpot_idx] + m_a[otherpot_idx][i])
print m_dp[full_s - 1][n - 1]
