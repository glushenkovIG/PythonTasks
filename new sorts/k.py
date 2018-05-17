A = list(map(int, input().split()))
B = list(map(int, input().split()))
i = 0
while i < len(A) - 1 and i < len(B) - 1 and A[i] == B[i]:
    i += 1
if i == len(A) - 1 and i == len(B) - 1:
    print('equal')
elif (i == len(A) - 1 and i != len(B) - 1):
    print('less')
elif (i != len(A) - 1 and i == len(B) - 1):
    print('greater')
elif A[i + 1] > B[i + 1]:
    print('less')
elif A[i + 1] < B[i + 1]:
    print('greater')