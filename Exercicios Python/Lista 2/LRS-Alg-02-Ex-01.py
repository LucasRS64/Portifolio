day = int(input("diga o tempo em dias: "))
hours = int(input("diga o tempo em horas: "))
min = int(input("diga o tempo em minutos: "))
sec = int(input("diga o tempo em segundos: "))

day_sec = 86400
hor_sec = 3600
min_sec = 60

conv1 = day_sec * day
conv2 = hor_sec * hours
conv3 = min_sec * min

conv_total = conv1 + conv2 +conv3 + sec

print(conv_total)


