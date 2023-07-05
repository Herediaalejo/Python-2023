import utils

def run():
    keys,values = utils.get_population()
    print(keys, values)

    data = [
        {
            "Country": "Argentina",
            "Population": 48000
        },
        {
            "Country": "Colombia",
            "Population": 60000
        }
    ]

    country = input("Introduzca el país => ")
    result = utils.population_by_country(data,country)
    print(result)

if __name__ == "__main__":
    run() # Entry point