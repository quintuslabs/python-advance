def star_args(*nums):
    total = 0
    for num in nums:
        total += int(num)
    return total
print(star_args(10,20,30))


def star_args2(*names):
    # for name in names:
    if 'sangram' in names and "sahoo" in names:
        print("welcome you are authorized to use the machine")
    else:
        print("sorry!!!you are unauthorized")

(star_args2('sk','sahoo','123'))
(star_args2('sangram','035172','sahoo'))

