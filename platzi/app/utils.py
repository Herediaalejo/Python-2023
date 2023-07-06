def population_by_country(data, country):
    country = country.title()
    result = list(filter(lambda item: item["Country/Territory"] == country, data))
    return(result)

def population_by_continent(data, continent):
    continent = continent.title()
    result = list(filter(lambda item: item["Continent"] == continent, data))
    return(result)

def get_population(data_country):
    population = {key.replace(" Population",""): int(value) for key, value in data_country[0].items() if "Population" in key and not "World Population Percentage" in key}
    labels = list(population.keys())
    values = list(population.values())
    return labels, values

def world_population(data):
    country = [data[i]["Country/Territory"] for i in range(len(data))]
    #country = list(map(lambda x:x["Country/Territory"], data))
    world_por = [data[i]["World Population Percentage"] for i in range(len(data))]
    #world_por = list(map(lambda x:x["World Population Percentage"], data))
    return country, world_por

def continent_population(data):
    country = [data[i]["Country/Territory"] for i in range(len(data))]
    world_por = [data[i]["World Population Percentage"] for i in range(len(data))]
    return country, world_por


