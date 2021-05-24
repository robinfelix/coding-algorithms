def maxhouses(A, B, tc):
  print (B)
  for i in range(len(A)):
    count = 0
    for j in range(i, len(A)):
      bud = A[j]
      if A[i] + bud  <= B:
        bud = bud + A[j]
        count += 1
  print("Case #{}: {}".format(tc, count))


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  N, B= [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
  A = [int(s) for s in input().split(" ")]
  maxhouses(A, B, i)
  # print("Case #{}: {} {}".format(i, N + B, N * B))
  # print(A)
  # check out .format's specification for more formatting options




# # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# # This is all you need for most problems.
# t = int(input()) # read a line with a single integer
# for i in range(1, t + 1):
#   n, m = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
#   print("Case #{}: {} {}".format(i, n + m, n * m))
#   # check out .format's specification for more formatting options