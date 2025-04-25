from functools import reduce

# level 1
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda i, i2: i + i2, numbers))

# level 2
complex_number = [[1, 2], [3, 4], [5]]
flat_numbers = reduce(lambda cn, cn2: cn + cn2, complex_number)
print(flat_numbers)

# level 3
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(reduce(
    lambda acc, word: {
        **acc,
        word: acc.get(word, 0) + 1
    }
    ,words
    ,{}
))

# level 4
input = [
    {'cat': 'fruit', 'val': 10},
    {'cat': 'vegetable', 'val': 5},
    {'cat': 'fruit', 'val': 7},
    {'cat': 'meat', 'val': 12},
    {'cat': 'vegetable', 'val': 3}
]

print(reduce(
    lambda acc, item: {
        **acc,
        item['cat']: acc.get(item['cat'], 0) + item['val']
    }
    ,input
    ,{}
))

#level 5
input_data = [
    {'cat': 'fruit', 'val': 10, 'active': True},
    {'cat': 'vegetable', 'val': 5, 'active': False},
    {'cat': 'fruit', 'val': 7, 'active': True},
    {'cat': 'meat', 'val': 12, 'active': True},
    {'cat': 'vegetable', 'val': 3, 'active': True}
]
print(reduce(
    lambda acc, item: {
        **acc,
        item['cat']: acc.get(item['cat'], 0) + item['val']
    }
    ,filter(lambda i: i['active'], input_data)
    ,{}
))

#level 6
input_data = [
    {'cat': 'fruit', 'val': 10, 'active': True},
    {'cat': 'vegetable', 'val': 5, 'active': False},
    {'cat': 'fruit', 'val': 7, 'active': True},
    {'cat': 'meat', 'val': 12, 'active': True},
    {'cat': 'vegetable', 'val': 3, 'active': True}
]
print(reduce(
    lambda acc, item: {
        **acc,
        item['cat']: {
            "count": acc.get(item['cat'], {}).get('count', 0) + 1,
            "sum": acc.get(item['cat'], {}).get('sum', 0) + item['val'],
        }
    }
    ,filter(lambda i: i['active'], input_data)
    ,{}
))
