ARBOLES_JAL = [
    {
        "nombre_comun": "Aceitunilla",
        "nombre_cien": "Foriestera tomentosa",
        "tamanio": "Pequeño",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 0
        
    },
    {
        "nombre_comun":"Anona de la costa",
        "nombre_cien": "Annona reticulata",
        "tamanio": "Mediano",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 0
    },
    {
        "nombre_comun":"Arrayán",
        "nombre_cien": "Psidium satorianum",
        "tamanio": "Pequeño",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 0
    },
    {
        "nombre_comun":"Ceiba",
        "nombre_cien": "Ceiba pentandra",
        "tamanio": "Grande",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 37.7
    },
    {
        "nombre_comun":"Cedro Blanco",
        "nombre_cien": "Cupressus lusitanica",
        "tamanio": "Grande",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 45.3
    },
    {
        "nombre_comun":"Cedro Rojo",
        "nombre_cien": "Cedrela odorata",
        "tamanio": "Grande",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 33.5
    },
    {
        "nombre_comun":"Fresno",
        "nombre_cien": "Fraxinus uhdei",
        "tamanio": "Grande",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 32.7
    },

    {
        "nombre_comun":"Guamúchil",
        "nombre_cien": "Pithecellobim dulce",
        "tamanio": "Grande",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 41.9
    },
    {
        "nombre_comun":"Guayabo",
        "nombre_cien": "Psidium guajava",
        "tamanio": "Pequeño",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 36.9
    },
    {
        "nombre_comun":"Jacaranda",
        "nombre_cien": "Jacaranda mimosifolia",
        "tamanio": "Mediano",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 36.4
    },
    {
        "nombre_comun":"Jinuicil Peludo",
        "nombre_cien": "Inga vera",
        "tamanio": "Mediano",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 43.2
    },
    {
        "nombre_comun":"Palmilla",
        "nombre_cien": "Podocarpus matudae",
        "tamanio": "Grande",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 0
    },
    {
        "nombre_comun":"Papelillo",
        "nombre_cien": "Bursera multijuga",
        "tamanio": "Pequeño",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 0
    },
    {
        "nombre_comun":"Pino albellano",
        "nombre_cien": "Pinus douglasiana",
        "tamanio": "Grande",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 0
    },
    {
        "nombre_comun":"Pinus escobetón",
        "nombre_cien": "Pinus devoniana",
        "tamanio": "Mediano",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 0
    },
    {
        "nombre_comun":"Primavera",
        "nombre_cien": "Tabebuia Donnell-Smithii",
        "tamanio": "Grande",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 0
    },
    {
        "nombre_comun":"Zarcillo",
        "nombre_cien": "Alvaradoa amorphoides",
        "tamanio": "Pequeño",
        "municipios_conabio": [],
        "regiones_koppen": [],
        "clorofila": 45.6
    }
]

def main(dict):
    
    tamanio = dict["tamanio"]
    municipio = dict["municipio"]

    arboles_compatibles = []
    txt_arboles = ""
    
    for arbol in ARBOLES_JAL:
        if arbol["tamanio"] == tamanio:
            arboles_compatibles.append(arbol) 
            txt_arboles = txt_arboles + arbol["nombre_comun"] + "\n"
    
    return { 'message': txt_arboles }


mensaje = main({"tamanio": "Pequeño", "municipio": "Guadalajara"})
print(mensaje)