input = open('input.txt', 'r')
output = open('output.txt', 'w')
days, parties = input.readline().split()
days = int(days)
parties = int(parties)
A = set()
weekends = set([i for i in range(6, days + 1, 7)]) | set([i for i in range(7, days + 1, 7)])
for i in range(parties):
    begin, step = input.readline().split()
    B = set([i for i in range(int(begin), days + 1, int(step))])
    A |= B
A -= weekends
output.write(str(len(A)))
input.close()
output.close()