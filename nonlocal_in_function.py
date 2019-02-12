def nonlocal_demo():
    inner = 10
    def nonlocal_demo_child():
        nonlocal inner
        inner += 100
        return inner
    return print(nonlocal_demo_child())
nonlocal_demo()

