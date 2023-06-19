def treelv(root):
  lv = [-1] * (N + 1)
  lv[root] = 0
  q = deque([root])
  while q:
    node = q.popleft()
    for n in tree[node]:
      if lv[n] == -1:
        q.append(n)
        lv[n] = lv[node] + 1
  return lv
