import random

list1 = ["alpha", "bravo", "charlie"]
print("The first list is filled with the following values:\n\t", end="")
for i in range(len(list1)):
    print(f"{list1[i]} ", end=" ")
print()

list1.append("Delta")
list1.append("Echo")

list2 = []
for n in range(5):
    list2.append(random.randrange(1, 51))

print('The second list is filled with the following values:\n\t', end = " ")

for m in range(len(list2)):
    print(f'{list2[m]}', end= " ")