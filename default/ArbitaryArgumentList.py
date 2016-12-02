
def concat(*args, sep="/"):
    return sep.join(args)

if __name__ == '__main__':
    print(concat("earth", "mars", "venus"))
    print(concat("earth1", "mars1", "venus", sep="."))