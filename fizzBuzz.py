# recorrer numeros del 1 al 50, si el numeri es multiplo de 3, mostrar Fizz, si es multiplo de 5, mostrar Buzz, si es multiplo de 3 y 5, mostrar FizzBuzz
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)