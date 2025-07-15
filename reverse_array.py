#Given an array, return a new array that contains the same elements in reverse order.
n=int(input())
arr=list(map(int,input().strip().split()))

arr.reverse()
print(arr)

