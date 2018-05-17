input = open('input.txt', 'r')
output = open('output.txt', 'w')
n = int(input.readline().rstrip())
languages = [''] * 1001
count = [0] * 1001
all_know = [''] * 1001
len_lang = 0
len_all = 0
for i in range(n):
    a = int(input.readline())
    for j in range(a):
        language = input.readline().rstrip()
        if language in languages:
            x = languages.index(language)
            count[x] += 1
            if count[x] == n:
                all_know[len_all] = language
                len_all += 1
        else:
            languages[len_lang] = language
            count[len_lang] = 1
            len_lang += 1
output.write(str(len_all) + '\n' + '\n'.join(all_know[:len_all]) + '\n' + str(len_lang) + '\n' + '\n'.join(languages[:len_lang]))
input.close()
output.close()