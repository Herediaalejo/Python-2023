import csv

def dict_whit_data(key, value):
    """Funcion que nos permite retornar un diccionario a partir de los valores de dos listas

    Args:
        key (list): clave que tendrá el diccionario
        value (list): valores que tendrá el diccionario

    Returns:
        dict: diccionario con datos de las listas
    """
    iterable = zip(key, value)
    country_dict = {key : value for key, value in iterable}
    return country_dict

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)   
        data = list(map(lambda value: dict_whit_data(header, value) ,reader))

        return data
    
if __name__ == '__main__':
    path = './app/data.csv'
    data = read_csv(path)
    print(data[0])