CREATE DATABASE IF NOT EXISTS trivia;

USE trivia;

CREATE TABLE IF NOT EXISTS Jugador (
    ID_JUGADOR INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(255) NOT NULL,
    INSTAGRAM VARCHAR(255),
    TELEFONO VARCHAR(255),
    PUNTAJE INT NOT NULL,
    TIEMPO DOUBLE NOT NULL
);

CREATE TABLE IF NOT EXISTS Pregunta (
    ID_PREGUNTA INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(255) NOT NULL,
    RESPUESTA_CORRECTA VARCHAR(255) NOT NULL,
    RESPUESTA_INCORRECTA1 VARCHAR(255) NOT NULL,
    RESPUESTA_INCORRECTA2 VARCHAR(255) NOT NULL,
    RESPUESTA_INCORRECTA3 VARCHAR(255) NOT NULL
);

INSERT INTO pregunta(NOMBRE, RESPUESTA_CORRECTA, RESPUESTA_INCORRECTA1, RESPUESTA_INCORRECTA2, RESPUESTA_INCORRECTA3) VALUES 
("¿En qué año se fundó el instituto?", "1983", "1987", "1993", "1980"), 
("¿Cuál fue el nombre del establecimiento educativo cuando se fundó?", "Complejo Facultativo de Enseñanza Superior San Francisco de Asís", "Instituto Educativo Superior Cura Brochero", "Instituto Superior Arturo Umberto Illia", "Escuela Mayor Facultativa Raúl Alfonsin"), 
("¿Cuántos fueron los fundadores?", "24", "16", "29", "12"), 
("¿En qué año se convierte en colegio nacional?", "1985", "1989", "1995", "2001"), 
("¿Cuántos directores tuvo el Instituto hasta la fecha?", "4", "7", "9", "12"), 
("¿Cuántas carreras se dictan actualmente en el ISAUI?", "6", "4", "9", "11"), 
("¿Cuál fue el primer número de teléfono del Instituto?", "41164", "52314", "34245", "79845"), 
("¿Qué es el workshop?", "Una técnica de venta", "Un lugar donde comprar cosas", "Una carrera", "Un estilo de vida"), 
("¿Qué carrera fue la pionera con los viajes en las materias de prácticas?", "Técnico y Guía Superior en Turismo", "Tecnicatura en Desarrollo de Software", "Diseño de Espacios", "Trekking"), 
("¿Cómo era el edificio educativo en sus comienzos?", "Una casa con 3 ambientes", "Una cafetería con 2 ambientes", "Una casa con tan solo 1 ambiente", "Una panadería de 5 ambientes"), 
("¿Qué tipo de instituto es el ISAUI?", "Instituto Público", "Instituto Privado", "Instituto Semi-privado", "Instituto Semi-público"), 
("¿A partir de qué año la cooperadora empezó a construir las aulas?", "1986", "1981", "1992", "2001"), 
("¿De dónde provenía el dinero?", "Del bono contribución de los padres", "Del bono contribución de los profesores", "Del gobierno nacional", "Del gobierno provincial"), 
("¿Quién fue el presidente de la cooperadora en el inicio de la institución?", "Sr. Gatica", "Sra. Graciela", "Sr. Augusto", "Carlos"), 
("¿Quién es la presidenta de la cooperadora actualmente?", "Daniela Maschio", "Gabriela Roldan", "Agustina Aperlo", "Elizabeth Afazani"), 
("¿Cómo logró convertirse en instituto nacional?", "Mediante la gestión del diputado Anselmo Pelaez", "Mediante la ayuda del gobernador Schiaretti", "Mediante el acuerdo con la UEPC", "Mediante la reunión de las escuelas de Carlos Paz");