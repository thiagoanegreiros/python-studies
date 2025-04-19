import pickle

data = ['a', 'b']

with open('file.data', 'wb') as file:
    pickle.dump(data, file)

with open('file.data', 'rb') as file:
    new_data = pickle.load(file)
    print(new_data)