num = [99, 34, 25, 56, 72]
print(num)
num[1] = 88
print(num)
#num=[99,34,25,56,72]
#FUNCION INSERT
num.insert(1, 77)
print(num)
#num=[99,77,34,25,56,72]
#FUNCION APPEND (Inserta un valor a la última posición de la lista )
num.append(100)
print(num)
#num=[99,77,34,25,56,72,100]
#FUNCIÓN EXTEND
num2 = [9, 8, 7]
num.extend(num2)
print(num)
#FUNCIÓN REMOVE
#num=[99, 77, 88, 25, 56, 72, 100, 9, 8, 7]
num.remove(100)
print(num)
#FUNCIÓN POP
#num=[99, 77, 88, 25, 56, 72, 9, 8, 7]
num.pop(2)
print(num)
#FUNCIÓN DEL
#num=[99, 77, 25, 56, 72, 9, 8, 7]
del num[0]
print(num)
#FUNCIÓN CLEAR
#num=[77, 25, 56, 72, 9, 8, 7]
num.clear()
print(num)
