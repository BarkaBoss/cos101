age = int(input('Enter your age'))
height = float(input('Enter your height'))

if height > 168:
    print('You are tall enough')
elif age > 17:
    print('You can join the ride after a waiver')
else:
    print('You do not qualify for this ride')