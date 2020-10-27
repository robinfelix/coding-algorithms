arr = [5,3,1,9,8,2,4,7]
def inefficient_buuble(arr):
    print("In efficient bubble sort since iteration didnt stop once its sorted ")
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return  arr

arr1 = [5,3,1,9,8,2,4,7]

def efficient_bubble(arr):
    print("Efficient bubble sort bcz the iteration stops once the list is sorted")
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i] ,arr[i+1] = arr[i+1], arr[i]
                print (arr)
    return arr

inefficient_buuble(arr)
efficient_bubble(arr1)

'''
reference :
https://www.geeksforgeeks.org/bubble-sort/
https://stackoverflow.com/questions/895371/bubble-sort-homework
'''