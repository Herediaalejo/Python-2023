import spacy
import pandas as pd

nlp = spacy.load("es_core_news_sm") #Carga el idioma español


#LEMATIZACION

texto = "En el juego, dos equipos de cinco jugadores luchan en un combate jugador contra jugador, cada equipo ocupando y defendiendo su mitad del mapa. Cada uno de los diez jugadores controla un personaje, conocido como campeón, con habilidades únicas y diferentes estilos de juego."

documento = nlp(texto)

for elemento in documento:
    if elemento.is_punct or elemento.is_stop or elemento.is_space: #Si el token es un signo de puntuacion, un conector o un espacio entonces lo saltea
        continue
    print(elemento)
    print(elemento.lemma_) #Me trae la palabra origen de la que deriva dicho token
    print("-")

texto2 = """
Primer Mandamiento
Amarás a Dios sobre todas las cosas.
Segundo Mandamiento
No tomarás el nombre de Dios en vano.
Tercer Mandamiento
Santificarás las fiestas.
Cuarto Mandamiento
Honrarás a tu padre y a tu madre.
Quinto Mandamiento
No matarás.
Sexto Mandamiento
No cometerás actos impuros.
Séptimo Mandamiento
No robarás.
Octavo Mandamiento
No darás falso testimonio ni mentirás.
Noveno Mandamiento
No consentirás pensamientos ni deseos impuros.
Décimo Mandamiento
No codiciarás los bienes ajenos.
"""

doc_mand = nlp(texto2)

lista_tokens_lemmas= []

for token in doc_mand:
    if elemento.is_punct or elemento.is_stop or elemento.is_space: #Si el token es un signo de puntuacion, un conector o un espacio entonces lo saltea
        continue
    lista_tokens_lemmas.append(token.lower_, token.lemma_.lower())

tokens_lemas_df = pd.DataFrame(lista_tokens_lemmas, columns=["Token", "Lema"])
tokens_lemas_df.head(15)



