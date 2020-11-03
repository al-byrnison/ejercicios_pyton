# 1.Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print('¡Hola Mundo!')

# 2. Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable
# y luego muestre por pantalla el contenido de la variable.

cadena = '¡Hola Mundo!'
print(cadena)

# 3. Escribir un programa que pregunte el nombre del usuario en la consola
# y después de que el usuario lo introduzca muestre por pantalla la cadena
# ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre_usuario = input('Cual es su nombre? \n')
print('¡Hola '+nombre_usuario)

# 4. Escribir un programa que pregunte el nombre del usuario en la consola
# y un número entero e imprima por pantalla en líneas distintas el nombre del
# usuario tantas veces como el número introducido.

nombre_usuario = input('Cual es su nombre? \n')
numero = int(input('Ingrese un numero entero: \n'))
print((nombre_usuario, ' ')*numero)

# 5. Escribir un programa que pregunte el nombre del usuario en la consola
# y después de que el usuario lo introduzca muestre por pantalla <NOMBRE>
# tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas
# y <n> es el número de letras que tienen el nombre.

nombre_usuario = input('Ingrese su nombre:\n')
print(nombre_usuario.upper())
print('su nombre tiene ', len(nombre_usuario), 'letras')

# 6. Escribir un programa que realice la siguiente operación aritmética
# ((3+2)/(2*5))**2.

resultado = ((3+2)/(2*5))**2
print('((3+2)/(2*5))**2 =', resultado)

# 7.Escribir un programa que pregunte al usuario por el número de horas
# trabajadas y el coste por hora. Después debe mostrar por pantalla la paga
# que le corresponde.

horas = int(input('Ingrese el numero de horas trabajadas:\n'))
valor_hora = int(input('Ingrese el valor por hora trabajada:\n'))
pago = valor_hora*horas
print('Pago: $'+str(pago))

# 8. Escribir un programa que lea un entero positivo, n, introducido por el
# usuario y después muestre en pantalla la suma de todos los enteros
# desde 1 hasta n. La suma de los n primeros enteros positivos puede
# ser calculada de la siguiente forma: suma=(n(n+1))/2

num_n = int(input('Ingrese un valor:\n'))
suma = (num_n*(num_n+1))/2
print('La suma de los valores desde 1 hasta su numero es:', suma)

# 9. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase Tu índice de masa corporal
# es <imc> donde <imc> es el índice de masa corporal calculado
# redondeado con dos decimales.

peso = float(input('Indique su peso en kg:\n'))
altura = float(input('Indique su altura en mt:\n'))
imc = peso/altura
print(round(imc, 2))

# 10. Escribir un programa que pida al usuario dos números enteros y muestre
# por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m>
# son los números introducidos por el usuario, y <c> y <r> son el cociente
# y el resto de la división entera respectivamente.

n = int(input('Ingrese un valor:\n'))
m = int(input('Ingrese otro valor:\n'))
c = n/m
r = n % m
print('el cociente es:', c, 'y el resto es:', r)

# 11. Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital
# obtenido en la inversión.

inversion = int(input('Ingrese valor a invertir:\n'))
tasa_anual = float(input('Ingrese la tasa anual:\n'))
años = float(input('Ingrese la cantidad de años:\n'))
capital = inversion+((inversion*tasa_anual)*años)
print('Capital obtenido: $', capital, 'por una inversion de: $', inversion)

# 12. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
# paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada
# paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa
# que lea el número de payasos y muñecas vendidos en el último pedido y calcule el
# peso total del paquete que será enviado.

can_p = int(input('Indique la cantidad de payasos:\n'))
can_m = int(input('Indique la cantidad de muñecas:\n'))
total = ((can_p*112)+(can_m*75))/100
print('peso del paquete:', total, 'kg')

# 13. Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece
# el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta
# finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada
# en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular
# y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.

deposito = int(input('Ingrese el valor del deposito:\n'))
ahorro = deposito*1.04
primero = ahorro
segundo = primero*1.04
tercero = segundo*1.04
print('valance primer año: $', round(primero, 2))
print('valance segundo año: $', round(segundo, 2))
print('valance tercer año: $', round(tercero, 2))

# 14. Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día
# tiene un descuento del 60%. Escribir un programa que comience leyendo el número
# de barras vendidas que no son del día. Después el programa debe mostrar el
# precio habitual de una barra de pan, el descuento que se le hace por no ser fresca
# y el coste final total.

barras = int(input('Ingrese cantidad de barras de pan: \n'))
precio_dia = barras*3.49
descuento = precio_dia*0.4
print('precio por', barras, 'barras de pan: $', round(precio_dia, 2))
print('precio por añejo -60%: $', round(descuento, 2))
