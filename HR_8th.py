n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
for i in range(n):  # Only go up to the second last element
    if arr[i] > arr[i + 1]:
        print(arr[i + 1])
        break