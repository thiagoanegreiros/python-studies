sample_set = { 1, 2, 2, 4 }
sample_list = [1 , 2, 2, 4]
sample_tuple = (1, 2, 2, 4)
sample_dict = {"a": 1, "b": 2}

print(sample_set)
print(sample_list)
print(sample_tuple)
print(sample_dict["a"])

for chave, valor in sample_dict.items():
    print(f'{chave} → {valor}')