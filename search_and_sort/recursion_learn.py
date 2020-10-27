def sample(i, msg):
    print("before func call in recursion :::::  ", msg )
    i += 1
    if i !=3:
        sample(i , msg + "first")
        sample(i , msg + "second")
        print ("value of i : ",i)
    print("after recursion call  : ", i)

sample(0, "I am ")