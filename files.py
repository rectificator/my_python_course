def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Juan", "Pilar", "El pollo Loco", "Rufo", "Orejasé"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def append():
    names = ["Pahvo"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    read()
    write()
    append()

if __name__ == '__main__':
    run()