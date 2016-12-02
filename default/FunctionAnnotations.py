def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ', ' + eggs

if __name__ == '__main__':
    print(f('spam'))