#Given an array of integers, calculate and return the average value.
n=int(input())
arr=list(map(int,input().strip().split()))[:n]
sum=0
for i in arr:
    sum+=i
avg=sum/n     
print(avg)
