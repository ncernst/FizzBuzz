import sys

try:
    n = sys.argv[1]
except IndexError:
    print("Please pick a numnber")
    n = input(">>>")

while not n.isdigit():
    print("Please try again using only numeric values.")
    n = input(">>>")

print("Fizz buzz counting up to " + str(n))

n = int(n)
i = 1

while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(str(i))
        
    i += 1
    