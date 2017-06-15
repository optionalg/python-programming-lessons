number = int(input("Enter a number: "))

i = 1
while i <= number:
    if number % i == 0:
        print(i)
    i = i + 1

# ---------

number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)
