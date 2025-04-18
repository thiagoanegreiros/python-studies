with open('test.txt', 'w') as file:
    file.write('hahaha\nhehehe')

with open('test.txt', 'r') as file:
    print(file.read())