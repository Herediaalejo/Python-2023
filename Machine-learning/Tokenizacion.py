import spacy

nlp = spacy.load("es_core_news_sm") #Carga el idioma español

texto = "Hola buenas tardes. Mi nombre es Alejo. Soy programador." #Genero un texto que va a ser analizado por la libreria nlp

documento = nlp(texto) #Analizo el documento a traves de la libreria spacy

#TOKENIZACION
for elemento in documento:
    print(elemento, elemento.pos_) #Imprimo cada elemento del documento que me analizo la libreria (siendo estos los tokens), ademas imprimo el tipo de palabra que es cada palabra del documento
    print(type(elemento)) #Me dice el que tipo de dato de cada elemento es token

print(spacy.explain("AUX")) #La libreria me explica que tipo de palabra es la que tiene las siglas AUX
print(spacy.explain("DET"))

for oracion in documento.sents: #.sents me divide el documento en oraciones
    print(oracion)
    print("-"*3)

for elemento in documento:
    print(elemento.lower_) #convierte cada token en minisculas
    print(elemento.is_punct) #Devuelve True o False dependiendo si el token es un signo de puntacion o no
    print("-"*3)

print(len(documento)) #Imprime la longitud del documento analizado

print(documento[0:4]) #Imprime los tokens del documento de la posicion 0 a 4




