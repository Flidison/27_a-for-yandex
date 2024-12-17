'''import csv,math
p=list(map(lambda x:list(map(float,x.rstrip().split())),open("27_A (2) исходник.txt","r").readlines()))
print(p)
ans=open("ssss.csv","w")
writer = csv.writer(
        ans, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
for i in p:
    if i[0]==90 or i[0]==270:
        writer.writerow([0.0, i[1] * math.sin(math.radians(i[0]))])
    else:
        writer.writerow([i[1]*math.cos(math.radians(i[0])),i[1]*math.sin(math.radians(i[0]))])'''
# Вверху с помощью питона переделывал точки из полярной системы в декардову. И записывал в бд ssss.csv
import turtle as t
from r5 import p  # Ответ не сходился, решил что, из-за ошибки в вычислениях с вещественными числами у питона

can = t.getcanvas()

cords = p
n = 0
k = 1

print(cords)
for i in cords:
    if i[0] < 0:
        can.create_oval(4 * i[0] - 1, 4 * i[1] - 1, 4 * i[0] + 1, 4 * i[1] + 1,
                        fill="red")                                                 # рисовал чтобы понять как разделить точки по кластерам
    else:
        can.create_oval(4 * i[0] - 1, 4 * i[1] - 1, 4 * i[0] + 1, 4 * i[1] + 1, fill="black")
can.create_line(0, -500, 0, 500)
can.create_line(-500, 0, 500, 0)
first = []
second = []
for i in cords:
    if i[0] < 0:
        first.append(i)
    else:
        second.append(i)


def sum(coords) -> []:  # Функция для определения центроидов
    mini = 10000000000000000
    ans = []
    for i in coords:
        num = 0
        for j in coords:
            num += (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
        if num < mini:
            mini = num
            ans = i
    return ans


a, b = sum(first), sum(second)
print(a, b)
print(10000 * (a[0] + b[0]) / 2)
print(10000 * (a[1] + b[1]) / 2)
t.mainloop()
