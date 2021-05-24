'''
reversal algorithm for array rotation
there are few more algorithm like block swap check in geek for geek
'''

arr = [1,2,3,4,5,6,7]
d = 2
n = 7

def reversearr(t_arr):
    return t_arr[::-1]

def solve(arr,d):
    # rev_A =  reversearr(arr[:d]) + arr[d:]
    rev_AB  = reversearr(arr[:d]) + reversearr(arr[d:])
    result_rev = reversearr(rev_AB)
    print (result_rev)

solve(arr, d)