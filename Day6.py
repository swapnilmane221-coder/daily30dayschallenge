def zero_subarrays(arr):
    prefix_sum = 0
    seen = {}   # map: prefix_sum -> list of indices where it appeared
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum == 0:
            result.append((0, i))

        if prefix_sum in seen:
            for start_index in seen[prefix_sum]:
                result.append((start_index + 1, i))

        seen.setdefault(prefix_sum, []).append(i)

    return result


arr=list(map(int,input().split()))
print(zero_subarrays(arr))

