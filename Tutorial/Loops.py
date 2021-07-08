#En python tenemos 2 tipos de iteradores

#FOR loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

#también podemos utilizar las funciones range y xrange
#La diferencia es que xrange es lazy.
for x in range(5):
    print(x) # Prints out the numbers 0,1,2,3,4

for x in range(3, 6):
    print(x) # Prints out 3,4,5

for x in range(3, 8, 2):
    print(x) # Prints out 3,5,7


#WHILE loop
count = 0
while count < 5:
    print(count)
    count += 1  # Prints out 0,1,2,3,4

#Soporta las palabras clave Break y continue.
count = 0
while True:
    print(count) # Prints out 0,1,2,3,4
    count += 1
    if count >= 5:
        break

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x) # Prints out only odd numbers - 1,3,5,7,9

#The ELSE case
#Podemos usar else en ambos loops. El código se ejecuta si la condición del loop falla.
#Si usamos un break dentro del loop, el código del bloque ELSE se ignora.
#Si usamos continue dentro del loop, el código del bloque ELSE se ejecuta de igual manera.

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")