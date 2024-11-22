#1.Найдите число, которое встречается только один раз в массиве
print("Task 1 ======================================")
def find_unic_num(nums):
    result = 0
    for num in nums:
        result ^=num #применение XOP побитовой операции (исключающая ИЛИ)
    return result

nums1 = [2,2,1]
nums2 = [4,1,2,1,2]
nums3 = [1]

print(find_unic_num(nums1))
print(find_unic_num(nums2))
print(find_unic_num(nums3))

#2.
print("Task 2 ======================================")
def bin_list(n):
    arr = list(range(n+1))
    for i in range(len(arr)):
        arr[i] = bin(arr[i]).count('1')
    return arr

num1 = 5
num2 = 2
num3 = 4

print(bin_list(num1))
print(bin_list(num2))
print(bin_list(num3))
