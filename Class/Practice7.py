# import string
# import re
# text= str(input())

# def split_text(text):
#     return text.split
# def clean_text(words_list):
#     result = []
#     for word in words_list:
#         new_word = ''
#         has_punctuation_mark = False
#         for ch in string.punctuation:
#             if ch in word:
#                 pos = word.find(ch)
#                 if pos == len(word) -1:
#                     new_word = word[:pos]
#                 elif pos < len(word):
#                     new_word = word[:pos] + word[pos+1:]
#                 has_punctuation_mark = True
#         if not has_punctuation_mark:
#             new_word = word
#         result.append(new_word.lower())
#     return result

# s = 'Патрис Лумумба, первый премьер-министр республики Конго (Леопольдвиль), выступил с речью во время официальной церемонии празднования независимости Республики Конго во Дворце Нации в Леопольдвиле (ныне — столица ДРК Киншаса).'

# def count_words(words_list):
#     set_words = set(words_list)
#     words_dict = {word : words_list.count(word) for word in set_words}
#     return words_dict
# def top_10(words_dict):
#     print('The top-10 words:')
#     items = words_dict.items()
#     items = sorted(items, key=lambda x : x[1], reverse = True)
#     for word, counter in items[:10]:
#         print(word, ': ', counter)
# top_10(count_words(clean_text(s.split())))



d={}
def validate_number(p):
    if len(p)!= 16:
        return False
    if not p[0:3] == '+7-':
        return False
    if not (p[6] == '-' and p[10] == '-' and p[13] == '-'):
        return False
    
    actual_phone = p[3:6] + p[7:10] + p[11:13] + p[14:]

    digits = '0123456789'
    for ch in actual_phone:
        if not ch in digits:
            return False
    return True

def add_to_book(name, phone):
    d[name] = phone

while True:
    name = str(input('Введите имя: '))
    if name == 'q':
        print(d)
        break
    phone = str(input('Введите номер: '))
    if phone == 'q':
        print(d)
        break
    if validate_number(phone):
        print ('Number is okey, adding to book..')
        add_to_book(name, phone)
        print('New phone added')
    else:
        print('Number is incorrect, please give another')