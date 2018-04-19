# Imprime numeros de 1 a 100, com hello no lugar do 3,
# world no lugar do 7 e se o numero for divisivel por 3 e 7, hello world.

number = 1
while number < 100:

    divBy3 = number % 3
    divBy7 = number % 7

    if number == 3:
        print "Hello"
    if number == 7:
        print "World"
    if divBy3 == 0 and divBy7 == 0:
        print "Hello World"
    else:
        print number

    number += 1
