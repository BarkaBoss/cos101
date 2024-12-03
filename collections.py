numbers = [13, 21, 6, 7, 90]
okpa_list = ['bambara nut',
             'maggie',
             'palm oil',
             'vegetable'
             ]
print(okpa_list)
okpa_list.append('fish')
print(okpa_list)

ingredient = input('Enter an ingredient')
for item in okpa_list:
    if item == ingredient:
        print(item, ' is in the list')

total = 0
for number in numbers:
    total = total + number

print(total)
print(numbers[2])