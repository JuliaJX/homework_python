# homework_python
#Программа для написания ФИО где ИО - только начальные буквы. Вариант 1
name = "Vinogradova Yulia Igorevna"
def initials (name):
    start = 0
    result =[]
    for i in range(len(name)):
            if name[i] == ' ':
                result.append(name[start:i])
                start = i + 1
            if i == len(name) - 1: 
                result.append(name[start:i])   
    return result[0] + ' ' + result[1][0:1] + '. ' + result[2][0:1] + '.'
print(initials(name)) 

#Вариантт 2
name = "Vinogradova Yulia Igorevna"
def initials (name):
    l=name.split()
    return l[0] + ' ' + l[1][0:1] + '. ' + l[2][0:1] + '.'
print(initials(name))   