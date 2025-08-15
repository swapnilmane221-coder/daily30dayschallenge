def sort(arr):
     i=0
     j=len(arr)-1
     k=0
     while k<=j:
          if arr[k]==0:
               arr[i],arr[k]=arr[k],arr[i]
               # print(arr,"0")
               i+=1
               k+=1
          elif arr[k]==2:
               arr[j],arr[k]=arr[k],arr[j]
               j-=1
               # print(arr,"2")
          else:
               k+=1
     return arr


arr=list(map(int,input().split()))
print(sort(arr))
