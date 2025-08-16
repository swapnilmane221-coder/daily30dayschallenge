def missingValue(arr):
     n=max(arr)
     # print(n)
     missing_num=(n*(n+1)//2)-sum(arr)
     if missing_num==0:
          return n+1
     return missing_num
     
arr=list(map(int,input().split()))
print(missingValue(arr))