# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_list = []
#
# for number in numbers:
#     if number < 5:
#         new_list.append(number)
#
# print(new_list)

# ---------------
maximum = int(input("Enter a number: "))
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([number for number in numbers if number < maximum])
