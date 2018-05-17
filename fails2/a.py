input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.read().split()
sum_ = 0
for i in range(len(a)):
    sum_ += int(a[i])
print(sum_, file = output)
input.close()
output.close()