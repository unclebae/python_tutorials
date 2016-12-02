# normal call with separate arguments
print(list(range(3, 6)))

# call with arguments unpacked from a list
args = [3, 6]
print(list(range(*args)))

# In the same faction, dictionaries can deliver keyword arguments with the **-operator:
def parrot(voltage, state="a stiff", action="voom"):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts throught it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state":"bleedin' demised", "action":"VOOM"}
parrot(**d)

