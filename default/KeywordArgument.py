def parrot(voltage, state='a stiff', action='voom', type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts throught it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print()

if __name__ == '__main__':
    parrot(1000)
    parrot(voltage=1000)
    parrot(voltage=1000000, action='VOOOOOOM')
    parrot(action="VOOOOM", voltage=1000000)
    parrot('a million', 'bereft of life', 'jump')
    parrot('a thousand', state='pushing up the daisies')