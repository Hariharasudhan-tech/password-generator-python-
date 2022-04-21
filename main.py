# A password generator project
import random
print('Welcome To The Password Generator! ')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()^_?'


number = int(input('Enter the numbers: '))

length = int(input('Enter the length of password u want: '))

print('\nHere are your passwords: ')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password, end='\n')
