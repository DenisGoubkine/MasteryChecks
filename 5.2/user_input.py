import random 

lottery = []

for i in range(6):
    lottery.append(random.randrange(0, 56))

lucky_number = int(input('What is your lucky number, provide ANY number you can think of from 1-55: '))
lottery.append(lucky_number)

print(f'Your winning lottery numbers are {lottery}')
