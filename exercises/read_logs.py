class ServerLog():
    def __init__(self, date, type, log):
        self.date = date
        self.type = type
        self.log = log

    def __str__(self):
        return f'My Log -> {self.date} - {self.type} - {self.log}'

logs = []
with(open('./exercises/logs', 'r')) as file:
    for l in file:
        c = l.strip().split('-')
        logs.append(ServerLog(c[0], c[3], c[4]))

for i in logs:
    print(i)