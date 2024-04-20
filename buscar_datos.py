import unittest

def buscar_datos(*args, **kwargs):
    arg_set = set(args) #conjunto (set) que contiene los valores pasados a la funcion a traves de argumentos. Se usan para comparar varios valores de forma simple.
    listado_personas = [] #lista para almacenar las personas cuyos datos coindicen con los datos buscados. La uso por si hay valores repetidos dentro de la base.

    for persona, datos in kwargs.items():
        datos_set = set(datos.values()) #conjunto de los valores del diccionario de cada persona.

        if arg_set.issubset(datos_set):       #verifica si los valores de los argumentos pasados son "subconjunto" de los datos contenidos en database.
            listado_personas.append(persona)  #es decir, compara los valores pasados y si encuentra que son parte de alguna persona en database, las agrega a listado_personas

    if listado_personas:
        return listado_personas 
    
    else:
        return "Los datos solicitados no se encuentran dentro de la base" #el codigo devuelve las llaves de las personas almacenadas en la lista, o un mensaje indicando que no encontro nada si la lista esta vacia

database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Juan",
        "segundo_nombre": "Carlos",
        "primer_apellido": "Perez",
        "segundo_apellido": "Sanchez"
    },
    "persona3": {
        "primer_nombre": "Juan",
        "segundo_nombre": "Pablo",
        "primer_apellido": "Gonzalez",
        "segundo_apellido": "Diaz"
    },
    "persona4": {
        "primer_nombre": "Alejandro",
        "segundo_nombre": "Lionel",
        "primer_apellido": "Romero",
        "segundo_apellido": "Sosa"
    },               
}

resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database) #solamente para verificar que el codigo funcione correctamente
print("llave:", resultado)

if __name__ == "__main__":
    unittest.main()
