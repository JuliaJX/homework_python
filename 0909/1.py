names = ["Иванов Степан Андреевич", "Долинин Константин Георгиевич", "Владимир Владимирович Путин"]
def initials (name):
    j=name.split()
    return j[0] + " " + j[1][0:1]+ '. ' + j[2][0:1] + '. '
def initials_more(name):
    return [initials(name) for name in names]

print(initials_more(names))
