def CountSort(A):
    amount_elem = [0] * 102
    final = []
    elements = []
    for elem in A:
        amount_elem[elem] += 1
    for i in range(102):
        elements = [i] * amount_elem[i]
        final.extend(elements)
    return final


A = list(map(int, input().split()))
print(' '.join(map(str, CountSort(A))))