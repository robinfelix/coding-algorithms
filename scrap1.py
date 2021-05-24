# def mala(limit):
#     if limit == 0:
#         return
#     print ("before mala", limit)
#     mala(limit = limit - 1)
#     print("malaaaaa : ", limit)
#
#
# mala(10)

A = [1,2,3,4]
for a, b in zip(A[::2], A[1::2]):
    print (a,b)