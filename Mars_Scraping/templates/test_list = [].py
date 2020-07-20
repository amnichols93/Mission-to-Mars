test_list = []
letters = ['a', 'b', 'c', 'd']
numbers = ['1', '2', '3', '4']

for letter in letters:
    for number in numbers:
        test_dict = {'letter': letter, 'number': number}
        test_list.append(test_dict)

print(test_list[0]['letter'])