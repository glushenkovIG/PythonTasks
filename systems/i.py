def bin2hex(a):
    ans = ''
    for i in range(0, len(a), 4):
        ans += table[a[i:i + 4]]
    return ans


a = input()[::-1]
while len(a) % 4 != 0:
    a += '0'
table = dict({'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'})
print(bin2hex(a[::-1]))