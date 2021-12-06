def divisors(numero):
    try:
        divisors = []
        if( numero < 0):
            raise ValueError("Debes ingresar un numero positivo")
        
        for i in range(1,numero+1):
            if numero % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return []


def run():
    try:
        numero = input(""" Introduce un número:
             """)
        numero = int(numero)
        print(divisors (numero))
    except ValueError:
        print("Debes ingresar un numero")


if __name__ == '__main__':
    run()