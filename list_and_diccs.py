def generate_name_dicc(firstName, lastName):
    return {'firstName': firstName, 'lasrName': lastName}



def run():
    my_list = [1 ,"Hello", True, 4.5]
    my_dicc = {'firstName': 'Juan', 'lasrName': 'Cuahonte'}

    #Lista de diccionarios
    super_list = [
        generate_name_dicc('Juan', 'Cuahonte'),
        generate_name_dicc('Miguel','Hernández'),
        generate_name_dicc('Rufo', 'Chavez'),
        generate_name_dicc('Pollo', 'Loco'),
        generate_name_dicc('Pahvo', 'Bonito'),
    ]

    #Diccionario de listas
    super_dicc = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-3,-5,65,8],
        "floating_nums": [2.1, 33.3, 0.5, -8.0]
    }

    for key, value in super_dicc.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()