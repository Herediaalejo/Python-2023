def get_population():
    keys = ["arg", "col"]
    values = [440, 500]
    return keys,values

def population_by_country(data, country):
    country = country.title()
    result = list(filter(lambda item: item["Country"] == country, data))
    return(result)