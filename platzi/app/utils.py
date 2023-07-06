def population_by_country(data, country):
    country = country.title()
    result = list(filter(lambda item: item["Country/Territory"] == country, data))
    return(result)

def get_population(data_country):
    population = {key: int(value) for key, value in data_country[0].items() if "Population" in key and not "World Population Percentage" in key}
    labels = list(population.keys())
    values = list(population.values())
    return labels, values

