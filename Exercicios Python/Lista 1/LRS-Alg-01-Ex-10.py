import math
a = float(input("qual valor o valor de a? "))
b = float(input("qual valor o valor de b? "))

soma = a + b 
diff = b - a
multi = a * b
div = a / b
restd = a % b
log = math.log10(a)
elev = math.pow(a, b)

print("a soma de a e b é " + soma)
print("a diferença quando b é subtraido de a é " + diff)
print("O produto de a por b é " + multi)
print("O quociente quando a é dividido por b " + div)
print("O resto quando a é dividido por b é " + restd)
print("O resultado de log10a é " + log)
print("O resultado de a^b é " + elev)