mesos = ["gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "decembre"]

print(mesos[0])
print(mesos[6])
print(len(mesos))

for i in range(len(mesos)):
    print(mesos[i])

mesos.append("mes_inventat")

for mes in mesos:
    print(mes)

mesos.sort()

for mes in mesos:
    print(mes)

primers_mesos = mesos[:6]
print(f'Primers mesos: {primers_mesos}')
segons_mesos = mesos[6:]
print(f'Següents mesos: {segons_mesos}')

primers_mesos.extend(segons_mesos)
print(primers_mesos)