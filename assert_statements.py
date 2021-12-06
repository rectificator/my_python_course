def divisors(numero):
    try:
        divisors = []
        assert numero > 0, "Debes ingresar un numero positivo"
        
        for i in range(1,numero+1):
            if numero % i == 0:
                divisors.append(i)
        return divisors
    except AssertionError as ass:
        print(ass)
        return []


def run():
    
    numero = input(""" Introduce un número:
            """)
    assert numero.isnumeric(), "Debes ingresar un numero"
    numero = int(numero)
    print(divisors (numero))

        


if __name__ == '__main__':
    run()