i = 0
mai = 0
med = 0
men = 0
while i < 10:
    x = int(input("digite um numero inteiro: "))
    if i == 0:
        mai = x
        men = x
    if (x > mai) :
        mai = x    
    elif (x < men) :
        men = x
    
    med = med + x
    i += 1

media = med / 10

print(f'O maior numero é {mai}')
print(f'A media entre os numeros é {media}')
print(f'O menor numero é {men}')
    