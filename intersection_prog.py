def intersection(l1,l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common
print(intersection(set([1,2,3,54,8,69,6,6]),set([7,8,91,4,5,7,4,8,8,5,2,6,2,5])))


def intersection_comp(l1,l2):
   return [val for val in l1 if val in l2]
print(intersection([1,5,4,7,89],[4,8,7,9,6,5,4,1,3]))

