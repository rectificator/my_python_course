def run():

    #for i in range(1,101):
    #    if i % 3 == 0:
    #        continue
    #    squares.append(i**2)
    #El codigo comentado arriba se puede resolver con una sola linea usando List Comprehensions

    squares = [i**2 for i in range(1,101) if i % 3 != 0]
    
    print(squares)

    multiple_of_4_6_and_9 = [i for i in range(9999999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 and len(str(i)) <= 5]

    print(multiple_of_4_6_and_9)

if __name__ == '__main__':
    run()