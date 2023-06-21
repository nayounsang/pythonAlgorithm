def mulmat(a,b,r):
  if len(b) != len(a[0]):
    raise IndexError
  result = [[0]*len(a) for _ in range(len(b[0]))]
  for i in range(len(a)):
    for j in range(len(b[0])):
      for k in range(len(b)):
        result[i][j] = (result[i][j] + a[i][k] * b[k][j] % r) % r
  return result

def powermat(m,p,r):
  result = deepcopy(m)
  while p > 0:
    if p & 1:
      result = mulmat(result,m,r)
    m = mulmat(m,m,r)
    p = p >> 1
  return result
        
