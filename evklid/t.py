def IsPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


a = int(input())
b = a
A = []
while not IsPrime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0 and IsPrime(i):
            A.append(i)
            a = a // i
            pass
if a != 1:
    A.append(a)
if b == 1:
    A.append(a)
A = sorted(A)
ans = A[0] - 1
for i in range(1, len(A)):
    ans *= A[i] - 1
    if A[i] == A[i - 1]:
        ans *= (A[i] / (A[i] - 1))
if b != 1 and b != 0:
    print(int(ans))
elif b == 1:
    print(1)

            
