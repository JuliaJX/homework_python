import random
surnames_list=['Федотов', 'Носов', 'Гвоздёв', 'Рассветный', 'Лебедев']
names_list=['Сергей', 'Богдан', 'Евгений', 'Алексей']
father_name=['Геннадьевич', 'Степанович', 'Николаевич', 'Росчеславович']
def generator_x(num):
    i = 0
    while i < num:
        yield random.choice(surnames_list) + ' ' + random.choice(names_list) + ' ' + random.choice(father_name)
        i += 1

gen = generator_x(3)
for x in gen:
    print(str(x))