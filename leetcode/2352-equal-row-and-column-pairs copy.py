input_data = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]

hash_map = {}

size = len(input_data)

for r in range(size):
    # Processa a linha
    row_items = [str(input_data[r][c]) for c in range(len(input_data[0]))]
    row_key = ''.join(sorted(row_items))
    hash_map[row_key] = hash_map.get(row_key, 0) + 1

    # Processa a coluna
    col_items = [str(input_data[c][r]) for c in range(size)]
    col_key = ''.join(sorted(col_items))
    hash_map[col_key] = hash_map.get(col_key, 0) + 1

print(hash_map)
