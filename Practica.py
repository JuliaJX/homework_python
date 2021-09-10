import string 

s=string.ascii_lowercase

f1=list(s)
f2=[]
for c in s:
    [f2.append(c)]


f3=[c for c in s]

print (f1)
print (f2)
print (f3)



