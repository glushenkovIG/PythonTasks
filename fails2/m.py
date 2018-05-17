input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.readline().rstrip()
count_letter = [0] * 26
x = ord('Z') - ord('A')
find = 'NO'
result = ''
count_ = 0
midl = ''
for i in range(ord('A'), ord('Z') + 1):
    count_ = a.count(chr(i))
    if count_ > 0:
        count_letter[i - ord('A')] = count_
        if count_ % 2 == 1 and find == 'NO':
            find = 'YES'
            midl = chr(i)
    result += count_ // 2 * chr(i)
output.write(result + midl + result[::-1])     
input.close()
output.close()