def leaders(arr):
     max=arr[-1]
     temp=[]
     temp.append(max)
     for i in range(len(arr)-2,-1,-1):
          if arr[i]>max:
               temp.append(arr[i])
               max=arr[i]
     temp=temp[::-1]
     return temp


arr=list(map(int,input().split()))
print(leaders(arr))