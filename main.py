import json


def main(dict):
    
    with open("arboles.json") as config_file:
        ARBOLES_JAL = json.load(config_file)

    with open("municipios.json") as config_file:
        KOPPEN = json.load(config_file)
    
    # Obtiene los parametros enviados en formato JSON
    tamanio = dict["tamanio"]
    municipio = dict["municipio"]

    # Valor inicial de variables locales
    observaciones = "Especie compatible con condiciones climáticas"
    arboles_compatibles = []
    txt_arboles = ""
    
    # Revisa el diccionario de arboles, si encuentra uno con caracteristicas climaticas y tamaño compatible lo añade a arboles_compatibles
    for arbol in ARBOLES_JAL:
        if arbol["tamanio"] == tamanio and KOPPEN[municipio] in arbol["regiones_koppen"]:
            arboles_compatibles.append(arbol) 

    # Ordena los arboles compatibles segun concentracion de clorofila, en el indice 0 queda el que tiene la mayor concentracion
    arboles_compatibles.sort(key=lambda p: p["clorofila"], reverse=True)

    # Si el arbol principal es nativo segun CONABIO cambiar variable observaciones
    if municipio in arboles_compatibles[0]["municipios_conabio"]:
        observaciones = "✅ Especie nativa CONABIO ✅"

    # Borrar llaves del diccionario, para ahorrar espacio en JSON de retorno
    del arboles_compatibles[0]["municipios_conabio"]
    del arboles_compatibles[0]["regiones_koppen"]

    for arbol in arboles_compatibles[1:]:
        # Estructura texto con informacion de los arboles secundarios
        txt_arboles = txt_arboles + "{} ({})".format(arbol["nombre_comun"],arbol["nombre_cien"])

        # Revisa si el resto de los arboles es nativo CONABIO, para agregar marca de verificación
        if municipio in arbol["municipios_conabio"]:
            txt_arboles = txt_arboles + " ✅\n"
        else:
            txt_arboles = txt_arboles + "\n"
            
    return { 'principal': arboles_compatibles[0], 'secundarios': txt_arboles, "nativo": observaciones }


mensaje = main({"tamanio": "Grande", "municipio": "Puerto Vallarta"})
print(mensaje)
