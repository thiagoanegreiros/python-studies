def filter_lines(file, log_type):
    with open(file, 'r') as mfile:
        for l in mfile:
            if log_type.lower() in l.lower():
                yield l.strip()
    
for linha in filter_lines("./train/logs.txt", "ERROR"):
    print(linha)
