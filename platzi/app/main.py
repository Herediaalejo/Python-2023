import utils
import read_csv as rc
import charts

def run():
    data = rc.read_csv("./app/data.csv")
    op = int(input("Introduzca la opcion que desea realizar\n1) Poblacion historia de un pais\n2) Porcentaje de poblacion mundial\n:"))
    if op == 1:
        country = input("Introduzca el país => ")
        result = utils.population_by_country(data,country)

        if len(result)>0:
            country_data = result 
            labels, values = utils.get_population(country_data)
            charts.generate_bar_chart(labels, values)
    elif op == 2 :
        op = int(input("¿Desea filtrar por region u obtener el global?\n1) Por continente\n2) Global\n:"))
        if op == 1:
            op = int(input("Continentes\n1) America del sur\n2) America del norte\n3) Europa\n4) Asia\n5) Africa\n6) Oceania\n:")) 
            if op == 1:
                data_continent = utils.population_by_continent(data, "South America")

            elif op == 2:
                data_continent = utils.population_by_continent(data, "North America")

            elif op == 3:
                data_continent = utils.population_by_continent(data, "Europe")

            elif op == 4:
                data_continent = utils.population_by_continent(data, "Asia")

            elif op == 5:
                data_continent = utils.population_by_continent(data, "Africa")

            elif op == 6:
                data_continent = utils.population_by_continent(data, "Oceania")
        
            labels,values = utils.world_population(data_continent)
        else:
            labels,values = utils.world_population(data)
        charts.generate_pie_chart(labels, values)

if __name__ == "__main__":
    run() # Entry point