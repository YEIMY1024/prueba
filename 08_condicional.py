#Condicional if
adivinar=50
numero=int(input("Sr usuario, digite un número: "))
if(numero>adivinar):
  print("Bájele el volumen")
elif(numero<adivinar):
  print("Subále el volumen")
else:
  print("VERDADERO")

print('La ejecución del IF termino')

#If anidado
if(numero >= adivinar):
  if(numero> adivinar):
    print("Coloque un número menor")
  else:
    print("Acertado!!!")
else:
  print('La ejecución del IF termino')