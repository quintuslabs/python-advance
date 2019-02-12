name2 = "sangram"
def test_scope2():
   global name2
   name2 = (f'{name2}  keshari sahoo')
   return name2


print(test_scope2())