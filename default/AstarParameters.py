# *arguments : list 로 데이터를 넣을 수 있다
# **keywords : dict 타입으로 데이터를 넣을 수 있다
# **아규먼트는 반드시 *뒤에 나와야한다

def cheeseshop(kind, *arguments, **keyword):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-"* 40)
    keys = sorted(keyword.keys())
    for kw in keys:
        print(kw, ":", keyword[kw])

if __name__ == '__main__':
    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")
