def kwargs_1(**args):
    for name,color in args.items():
        print(f"{name} 's favourit color is {color}")
(kwargs_1(sangram = 'black',pupi ='white',jani = 'red' ))


def kwargs_2(**argss):
    if "sangram" in argss and argss["sangram"] == "special":
        print("you are our special guest!!!! welcome sir ,have a goog party")
    elif 'arjun' in argss:
        print("yes sir you can come in..your number is in our list")
    else:
        print("sorry your name is not in our list.")
kwargs_2(sangram = 'special')
kwargs_2(sangram = 'hello')
