Anya, Borya = input().split()
anya = set()
borya = set()
for i in range(int(Anya)):
    anya.add(input())
for i in range(int(Borya)):
    borya.add(input())
a_b = anya & borya
print(len(a_b))
print(' '.join(list(map(str, sorted(map(int, (a_b)))))))
print(len(anya - a_b))
print(' '.join(list(map(str, sorted(map(int, (anya - a_b)))))))
print(len(borya - a_b))
print(' '.join(list(map(str, sorted(map(int, (borya - a_b)))))))