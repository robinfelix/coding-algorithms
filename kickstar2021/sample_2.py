





def solve(G):
  count = 0
  temp = 0
  for k in range(1,G+1):
    for d in range(1,G+1):
      temp = temp + k
      if G == temp + d:
        count += 1
  print(count)








t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  G = int(input())
  solve(G)