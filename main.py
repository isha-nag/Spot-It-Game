import random

my_list = random.sample("abcdefghijklmnopqrstuvwxyz", 10)


first_slice = my_list[:5]

second_slice = my_list[4:-1]

random.shuffle(first_slice)
random.shuffle(second_slice)

colors = ['\x1b[5;37;41m', '\x1b[5;37;42m', '\x1b[5;30;43m',  '\x1b[5;37;44m',  '\x1b[5;37;45m',  '\x1b[5;37;46m']

random.shuffle(colors)
for i in range(len(first_slice)):
    print(colors[i] + first_slice[i], end='')

print('\033[0m')

random.shuffle(colors)
for i in range(len(second_slice)):
    print(colors[i] + second_slice[i], end='')

print('\033[0m')


answer = input("What is the common letter?")
print(answer)

while answer != my_list[4]:
    print("Incorrect!")
    answer = input("Try again!")
    print(answer)

print("Correct!")