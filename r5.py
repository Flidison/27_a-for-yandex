p = open("27_A (1)(Лист1)excel.csv", "r").readlines()
print(p)
for i in range(1000):
    p[i] = list(map(float, p[i].rstrip().replace(",", ".").split(";")[5:]))
print(p)
''' Делал эту таблицу в Excel сначала брал угол из первого столбца и преобразовывал в радианы(4-ый столбец) а дальше с помощью этого в X и Y (6,7 столбцы)'''
