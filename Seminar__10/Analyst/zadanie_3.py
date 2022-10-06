# Дан текст: в первой строке записано число строк, далее идут сами 
# строки. Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов или символами конца строки.
# Sample Input:
# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
# Sample Output:
# 19
# text = set()
# [text.update(input("Введите строку: ").split()) for i in range(int(input("Введите количество строк: ")))]
# print(len(text))

words = set()
for _ in range(int(input())):
    words.update(input().split())
    print(words)
print(len(words))