import os

files = ['file1', 'file2', 'train/any-all.py']

existsAny = any(os.path.exists(file) for file in files)
existsAll = all(os.path.exists(file) for file in files)

print(f'existsAny -> {existsAny}')
print(f'existsAll -> {existsAll}')
