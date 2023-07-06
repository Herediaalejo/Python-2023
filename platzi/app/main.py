import utils
import read_csv as rc
import charts

def run():
    data = rc.read_csv("./app/data.csv")
    country = input("Introduzca el país => ")

    result = utils.population_by_country(data,country)

    if len(result)>0:
        country_data = result 
        labels, values = utils.get_population(country_data)
        charts.generate_bar_chart(labels, values)

if __name__ == "__main__":
    run() # Entry point