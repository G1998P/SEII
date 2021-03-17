l = [1,4,3,2,10,65,3]

l2 = sorted(l)
print(l2)
print(l)#l nao for ordenada


t = tuple(l)

print(sorted(t))



d = []

for i in range(len(l)):
    d.append({'name':f'pessoa{i}','age':l[i]})


dd2 = sorted(d,key=lambda a:a['age'])
for pessoa in dd2:
    nome , idade = pessoa.values()
    print(nome,idade)
