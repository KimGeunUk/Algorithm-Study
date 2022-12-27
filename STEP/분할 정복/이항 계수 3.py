N, K = map(int, input().split())

def fac(n):
  res = 1
  for i in range(1,n+1):
    res = (res * i) % 1000000007

  return res


print(fac(N) // (fac(K) * fac(N-K)))