from datetime import date

myInteger = 5
print(myInteger)

myFloat = 5.1
print(myFloat)

myDate = date.today()
print(myDate)

def countdown(i) :
    for j in range(1, i+1):
        print(j, end = " ")
    print()

countdown(10)
countdown(5)
countdown(3)

print(3 > "blue")