def binSearch (array, val):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if (val == array[mid]):
            return mid
        elif val < array[mid]:
            high = mid - 1 
        else:
            low = mid + 1

    return 0 

nums = list(map(int, input().split()))
nums.sort()
counter = 0
# for i in range(len(nums)):
#     if binSearch(nums, nums[i]) == 0:
#         print(i, counter)
#         counter += 1
    
# print(counter)
# if counter > 0:
#     print("true")
# else:
#     print("false")
for i in range (len(nums)):
    for j in range (i + 1, len(nums)):
        if nums[i] == nums[j]:
            counter += 1
            
if counter > 0:
    print("true")
else:
    print("false")