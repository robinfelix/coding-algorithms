



def is_palindrome(com_value):
  if com_value == com_value[::-1]:
    return True
  return False

def solve(A, N, K, tc):
  from itertools import permutations
  alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

  comb = list(permutations(alphabet[:K], N))
  count = 0
  for i in comb:
    if str(A) < ''.join(i):
      print(''.join((i)))
      if is_palindrome(''.join(i)):
        # print (''.join(i))
        count += 1
  print("Case #{}: {}".format(tc, count))










t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  N, K= [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
  A = [s for s in input()]
  solve(A, N, K, i)