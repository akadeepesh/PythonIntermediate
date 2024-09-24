# arr = [1, 2, 2, 2, 2, 3]
# x = 2
# count = 0
# for i in arr:
#     if(i == x):
#         count += 1
# print(f"{x} occur {count} times in array")


arr = [1, 1, 2, 2, 2, 2, 3]
x = 2

def CalculateOccurrence(arr, x, n, findFirst: bool):
    low = 0
    high = n-1
    result = -1
    while low <= high:
        mid = (low+high)//2
        # If mid value is equal to target value
        if(arr[mid] == x):
            result = mid
            if(findFirst):
                high = mid - 1
            else:
                low = mid + 1
        # If mid value is smaller than target value
        elif(arr[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return result

first_index = CalculateOccurrence(arr, x, len(arr), True)
if(first_index == -1):
    print(f"{x} occurr 0 times in list")
else:
    last_index = CalculateOccurrence(arr, x, len(arr), False)
    print(f"{x} occurr {last_index - first_index + 1} times in list")