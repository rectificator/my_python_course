def run():

    #for i in range(1,101):
    #    if i % 3 != 0:
    #        cubes[i] = i**3
    #El codigo comentado arriba se puede resolver con una sola linea usando Dictionary Comprehensions
    cubes = {i:i**3 for i in range(1,101) if i%3 != 0}

    print(cubes)

    square_roots = {i:i**(1/2) for i in range(1,1001)}

    print(square_roots)

if __name__ == '__main__':
    run()
