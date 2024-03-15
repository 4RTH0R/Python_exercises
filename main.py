import os
import sys

#Setting clearing/restarting console
os.system('clear')
system = 'cls' if os.name == 'nt' else 'clear'
os.system(system)
print("Este é um conversor de unidades de temperatura")
tipo = input("Selecione a finalidade da conversão  - 'Celsius = 1 | Fahrenheit = 2 | Kelvin = 3': ")
#Verification/input
try: 
  as_int = int(tipo)
except ValueError:
  input("Medida não identificada | Aperte enter para reiniciar: ")
  #Clear/restart functions
  os.system('clear')
  os.execv(sys.executable, ['python'] + sys.argv)
if tipo == 1:
    s = int(input("Qual a sua medida? - 'Fahrenheit = 1 | Kelvin = 2': "))
    if s == 1:
      t = input("Insira a temperatura: ")
      t = float(t)
      c = round((float(t) - 32) * (5/9))
      print(f"A seguinte temperatura em Fahrenheit: '{t}',equivale a seguinte temperatura em celsius: '{c}'")
    elif s == 2:
      t = input("Insira a temperatura: ")
      t = float(t)
      c = round(t - 273.15)
      print(f"A seguinte temperatura em Kelvin : '{t}', equivale a seguinte temperatura em celsius: '{c}'")
    else:
      input("Medida não identificada | Aperte enter para reiniciar: ")
      os.system('clear')
      os.execv(sys.executable, ['python'] + sys.argv)
elif tipo == 2: #Elif set seconds conditions to be checked
    s = int(input("Qual a sua medida? - 'Celsius = 1 | Kelvin = 2': "))
    if s == 1:
      t = input("Insira a temperatura em Celsius: ")
      t = float(t)
      c = round((t - 32)/1.8)
      print(f"A seguinte temperatura em Celsius: '{t}',equivale a seguinte temperatura em Fahrenheit: '{c}'")
    elif s == 2:
      t = input("Insira a temperatura: ")
      t = float(t)
      c = round((t - 273.15) * 9/5 + 32)
      print(f"A seguinte temperatura em Kelvin: '{t}', equivale a seguinte temperatura em Fahrenheit: '{c}'")
    else:
      input("Medida não identificada | Aperte enter para reiniciar: ")
      os.system('clear')
      os.execv(sys.executable, ['python'] + sys.argv)
elif tipo == 3:
    s = int(input("Qual a sua medida? - 'Celsius = 1 | Fahrenheit = 2': "))
    if s == 1:
      t = input("Insira a temperatura em Celsius: ")
      c = round(float(t) + 273.15)
      print(f"A seguinte temperatura em Celsius : '{t}',equivale a seguinte temperatura em Kelvin: '{c}'")
    elif s == 2:
        t = float(input("Insira a temperatura em Fahrenheit: "))
        c = round(((t - 32)/1.8) + 273.15)
        print(f"A seguinte temperatura em Fahrenheit: '{t}',equivale a seguinte temperatura em Kelvin: '{c}'")
    else:
      input("Medida não identificada | Aperte enter para reiniciar: ")
      os.system('clear')
      os.execv(sys.executable, ['python'] + sys.argv)
else:
  print("Tipo de medida inválido")  
  answer = input("Deseja reiniciar o programa? (y/n): ")
  if answer.lower() == "y":
    os.system('clear')
    os.execv(sys.executable, ['python'] + sys.argv)
  else:
    input("Programa encerrado. Pressione Enter para reiniciar")
    os.system('clear')
    os.execv(sys.executable, ['python'] + sys.argv)
input("Fim do programa | Aperte enter para reiniciar")
os.system('clear')
os.execv(sys.executable, ['python'] + sys.argv)