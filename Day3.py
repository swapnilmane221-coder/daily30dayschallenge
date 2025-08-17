def duplicate(arr):
     if arr==[]:
          return []
     # print((max(arr)*(max(arr)+1))//2)
     return sum(arr)-((max(arr)*(max(arr)+1))//2)

arr=list(map(int,input().split()))
print(duplicate(arr))