m = int(input ("Введите длину шоколадки: "))
n = int(input ("Введите ширину шоколадки: "))
k = int(input ("Сколько долек нужно отломить: "))

if (k > (m * n)):
    print ("Долек, которые нужно отломить больше, чем долек в шоколадке!")
elif (k == m * n):
    print ("Можешь не отламывать, все уже сделано!")
elif (k % m == 0 or k % n == 0):
    print ("Можно отломить!")
else:
    print ("Отломить нельзя!")