import matplotlib.pyplot as plt # pip install matplotlib


# funcion para grafico de barra
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
    
# funcion para grafico de torta
def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()

if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [100, 20, 800]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels,values)

