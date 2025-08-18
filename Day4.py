def sort(arr1, arr2):
    n, m = len(arr1), len(arr2)
    gap = (n + m + 1) // 2   # initial gap

    while gap > 0:
        i = 0
        j = gap
        while j < n + m:
            
            if i < n:
                a = arr1[i]
            else:
                a = arr2[i - n]

            
            if j < n:
                b = arr1[j]
            else:
                b = arr2[j - n]

            if a > b:
                if i < n and j < n:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                elif i < n and j >= n:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
                else:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]

            i += 1
            j += 1

        gap = 0 if gap == 1 else (gap + 1) // 2

    return arr1, arr2


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(sort(arr1, arr2))
