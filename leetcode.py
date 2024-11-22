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