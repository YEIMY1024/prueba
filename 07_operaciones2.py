#OPERACIONES RELACIONALES O DE COMPARACIÓN
number = int(input('Digite un número: '))
print(number > 3)  #Pregunta si number es mayor que 3
print(number >= 3)  #Pregunta si number es mayor o igual que 3
print(number < 3)  #Pregunta si number es menor que
print(number <= 3)  #Pregunta si number es menor o igual que 3
print(number != 3)  #Pregunta si number es diferente que 3
print(number == 3)  #Pregunta si number es gual que 3

#****OPERACIONES LÓGICAS****
#True(1)/ False(0)
print('Operaciones lógicas')

#Conjunción (and &)
print(" ")
print("Conjución:")
print(True and False)
print((number >= 3) and False)

#Disyunción (or, |)
print(" ")
print("Disyunción")
print(False or False)
print(True or False or False)
print(number > 3 or True)
print(number > 3 | number < 10)

#Negación (not)
print(" ")
print("Negación")
print(not (True))

#Or exclusiva (^)
print(" ")
print("Or exclusiva")
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

#****OPERACIONES DE PERTENENCIA ***
# in
nombre ='Yeimy Lozano'
print('m' in nombre)