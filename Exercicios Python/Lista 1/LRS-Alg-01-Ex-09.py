val = float(input("qual valor deseja investir? "))

invst1 = val * (1+0.12)
invst2 = invst1 * (1+0.12)
invst3 = invst2 * (1+0.12)

print("***********************************************")
print("*")
print(f' valor após 1 ano: {invst1:.2f}')
print(f' valor após 2 anos: {invst2:.2f}')
print(f' valor após 3 anos: {invst3:.2f}')
print("*")
print("***********************************************")
