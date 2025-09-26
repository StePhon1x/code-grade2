n, k = map(int, input().split())
st = sf = nt = nf = 0

for i in range(1, n + 1):
    if i % k == 0:
        st += i
        nt += 1
    else:
        sf += i
        nf += 1

avg_t = st / nt if nt else 0.0
avg_f = sf / nf if nf else 0.0

print(f"{avg_t:.1f} {avg_f:.1f}")
