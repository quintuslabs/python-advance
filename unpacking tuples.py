def unpacking(*args):
    total = 0
    for num in args:
        total += num
    return total
# print(unpacking(10,20,30))
nums = [10,50,60,80]
nums1 = (10,50,60,80)
print(unpacking(*nums))
print(unpacking(*nums1))
