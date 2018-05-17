input = open('input.txt', 'r')
output = open('output.txt', 'w')
cities = dict()
n = int(input.readline())
for i in range(n):
    a = input.readline().split()
    for j in range(1, len(a)):
        cities[a[j]] = a[0]
n = int(input.readline())
for i in range(n):
    output.write(cities[input.readline().rstrip()] + '\n')
input.close()
output.close()