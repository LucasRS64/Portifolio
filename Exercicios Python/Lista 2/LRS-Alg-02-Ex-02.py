x = int(input("qual o valor em segundos? "))

day = 86400
hor = 3600
min = 60

conv1 = x // day
x2 = x % day 
conv2 = x2 // hor 
x3 = x2 % hor
conv3 = x3 // min 
x4 = x3 % min 

print(f'{conv1:02d}:{conv2:02d}:{conv3:02d}:{x4:02d}')