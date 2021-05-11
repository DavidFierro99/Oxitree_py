def main(dict):

    ARBOLES_JAL = [
        {
            "nombre_comun": "Aceitunilla",
            "nombre_cien": "Foriestera tomentosa",
            "tamanio": "Pequeño",
            "municipios_conabio": [],
            "regiones_koppen": ['CWA'],
            "clorofila": 0
            
        },
        {
            "nombre_comun":"Anona de la costa",
            "nombre_cien": "Annona reticulata",
            "tamanio": "Mediano",
            "municipios_conabio": ["Mascota", "Puerto Vallarta", "Cabo Corrientes", "Tomatlán", "Talpa de Allende", "Atenguillo", "Villa Purificación", "Autlán de Navarro", "Casimiro Castillo", "La Huerta", "Cihuatlán", "Cuautitlán de García Barragán", "Tolimán", "Tuxcuacuesco", "El Grullo", "El Limón", "Ejutla", "Tonaya", "Zapotitlán de Vadillo", "Tuxpan", "Tonila", "Pihaumo", "Zapoltitic", "Jilotlán de los Dolores", "Santa María del Oro", "Valle de Juárez", "Tamazula de Gordiano", "Poncitlán", "Chapala", "Jamay", "Ocotlán", "La Barca", "Zapotlán del Rey", "Ixtlahuacán de los Membrillos", "Tlajomulco de Zúñiga", "Villa Corona", "Cocula", "Atenguillo", "Atengo", "Tenamaxtlán", "Unión de Tula"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0
        },
        {
            "nombre_comun":"Arrayán",
            "nombre_cien": "Psidium satorianum",
            "tamanio": "Pequeño",
            "municipios_conabio": ["San Martín de Bolaños"", ""Atotonilco el Alto", "Ayotlán", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Jocotepec", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Jilotlan de los Dolores", "Pihuamo", "San Gabriel", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Zapotlán el Grande", "Atengo", "Autlán de Navarro", "Ayutla", "Chiquilistlán", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Cihuatlán", "Cuautitlán de García Barragán", "La Huerta", "Tomatlán ", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Teuchitlán", "Acatlán de Juárez", "Amacueca", "Atemajac de Brizuela", "Cocula", "San Martín Hidalgo", "Sayula", "Tapalpa", "Techaluta de Montenegro", "Teocuitatlán de Corona", "Villa Corona", "Zacoalco de Torres", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0
        },
        {
            "nombre_comun":"Ceiba",
            "nombre_cien": "Ceiba pentandra",
            "tamanio": "Grande",
            "municipios_conabio": ["Puerto Vallarta", "San Sebastían del Oeste", "Cabo Corrientes", "Tomatlán", "Villa Purificación", "La Huerta", "Casimiro Castillo", "Cihuatlán", "Tolimán", "Tuxpan", "Pihuamo", "Tuxcacuesco", "El Grullo", "El Limón", "Ejutla", "Tonaya", "Juchitlán", "Tenamaxtlán", "San Juanito de Escobedo", "Amatitán", "Teuchitlán", "Ahualulco de Mercado", "Zapotiltic", "Zapotlán el Grande"],
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
            "municipios_conabio": ["Unión de San Antonio", "San Diego de Alejandría", "San Julián", "Lagos de Moreno", "Arandas", "Jesús María", "Degollado", "Atotonilco el Alto", "Tepatitlán de Morelos", "San Ignacio Cerro Gordo", "San Miguel el Alto", "Acatic", "Zapotlanejo", "Juanacatlán", "Poncitlán", "Chapala", "Jocotepec", "Tuxcueca", "Tizapán el Alto", "Tlajomulco de Zúñiga", "Zacoalco de Torres", "Villa Corona", "Cocula", "Quitupan", "Valle de Juárez", "Mazamitla", "La Manzanilla de la Paz", "Concepción de Buenos Aires", "Atoyac", "Gómez Farías", "Atemajac de Brizuela", "Tecolotlán", "Tenamaxtlán", "Juchitlán", "Chiquilistlán", "Tapalpa", "San Gabriel"],
            "regiones_koppen": ['CWA', 'CWB'],
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
            "municipios_conabio": ["Bolaños", "Chimatitlan", "Colotlán", "Huejúcar", "Huejuquilla el Alto", "Mezquitic", "San Martín de Bolaños", "Santa María de los Ángeles", "Totatiche", "Villa Guerrero", "Encarnacion de Diaz", "Lagos de Moreno", "San Diego de Alejandría", "San Juan de los Lagos", "Union de San Antonio ", "Villa Hidalgo", "Acatic", "Arandas", "Cañadas de Obregón", "Jalostotitlán", "Jesús María", "Mexticacan", "San Ignacio Cerro Gordo", "San Julían", "San Miguel el Alto", "Tepatitlán de Morelos", "Valle de Guadalupe", "Yahualica de Connzález Gallo", "Atotonilco el Alto", "Ayotlán", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Concepción de Buenos Aires", "Jocotepec", "La Manzanilla de la Paz", "Mazamitla", "Quitupan", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Valle de Juárez", "Gómez Farias", "Jilotlan de los Dolores", "Pihuamo", "San Gabriel", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Zapotlán el Grande", "Atengo", "Autlán de Navarro", "Ayutla", "Chiquilistlán", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Cihuatlán", "Cuautitlán de García Barragán", "La Huerta", "Tomatlán ", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Amacueca", "Atemajac de Brizuela", "Atoyac", "Cocula", "San Martín Hidalgo", "Sayula", "Tapalpa", "Techaluta de Montenegro", "Teocuitatlán de Corona", "Villa Corona", "Zacoalco de Torres", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'BSH', 'AW'],
            "clorofila": 41.9
        },
        {
            "nombre_comun":"Guayabo",
            "nombre_cien": "Psidium guajava",
            "tamanio": "Pequeño",
            "municipios_conabio": ["Bolaños", "Chimatitlan", "Colotlán", "Huejúcar", "Huejuquilla el Alto", "Mezquitic", "San Martín de Bolaños", "Santa María de los Ángeles", "Totatiche", "Villa Guerrero", "Encarnacion de Diaz", "Lagos de Moreno", "San Diego de Alejandría", "San Juan de los Lagos", "Union de San Antonio ", "Villa Hidalgo", "Acatic", "Arandas", "Cañadas de Obregón", "Jalostotitlán", "Jesús María", "Mexticacan", "San Ignacio Cerro Gordo", "San Julían", "San Miguel el Alto", "Tepatitlán de Morelos", "Valle de Guadalupe", "Yahualica de Connzález Gallo", "Atotonilco el Alto", "Ayotlán", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Concepción de Buenos Aires", "Jocotepec", "La Manzanilla de la Paz", "Mazamitla", "Quitupan", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Valle de Juárez", "Gómez Farias", "Jilotlan de los Dolores", "Pihuamo", "San Gabriel", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Zapotlán el Grande", "Atengo", "Autlán de Navarro", "Ayutla", "Chiquilistlán", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Cihuatlán", "Cuautitlán de García Barragán", "La Huerta", "Tomatlán ", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Amacueca", "Atemajac de Brizuela", "Atoyac", "Cocula", "San Martín Hidalgo", "Sayula", "Tapalpa", "Techaluta de Montenegro", "Teocuitatlán de Corona", "Villa Corona", "Zacoalco de Torres", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 36.9
        },
        {
            "nombre_comun":"Jacaranda",
            "nombre_cien": "Jacaranda mimosifolia",
            "tamanio": "Mediano",
            "municipios_conabio": [],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 36.4
        },
        {
            "nombre_comun":"Jinuicil Peludo",
            "nombre_cien": "Inga vera",
            "tamanio": "Mediano",
            "municipios_conabio": [],
            "regiones_koppen": ['AW'],
            "clorofila": 43.2
        },
        {
            "nombre_comun":"Palmilla",
            "nombre_cien": "Podocarpus matudae",
            "tamanio": "Grande",
            "municipios_conabio": [],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0
        },
        {
            "nombre_comun":"Papelillo",
            "nombre_cien": "Bursera multijuga",
            "tamanio": "Pequeño",
            "municipios_conabio": ["Bolaños", "Chimatitlan", "Colotlán", "Huejúcar", "Huejuquilla el Alto", "Mezquitic", "San Martín de Bolaños", "Santa María de los Ángeles", "Totatiche", "Villa Guerrero", "San Diego de Alejandría", "San Juan de los Lagos", "Teocaltiche", "Union de San Antonio ", "Villa Hidalgo", "Acatic", "Arandas", "Cañadas de Obregón", "Jalostotitlán", "Jesús María", "Mexticacan", "San Ignacio Cerro Gordo", "San Julían", "San Miguel el Alto", "Tepatitlán de Morelos", "Valle de Guadalupe", "Yahualica de Connzález Gallo", "Atotonilco el Alto", "Ayotlán", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Concepción de Buenos Aires", "Jocotepec", "La Manzanilla de la Paz", "Mazamitla", "Quitupan", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Valle de Juárez", "Gómez Farias", "Jilotlan de los Dolores", "Pihuamo", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Zapotlán el Grande", "Atengo", "Autlán de Navarro", "Ayutla", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Amacueca", "Atoyac", "Cocula", "San Martín Hidalgo", "Sayula", "Techaluta de Montenegro", "Teocuitatlán de Corona", "Villa Corona", "Zacoalco de Torres", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0
        },
        {
            "nombre_comun":"Pino albellano",
            "nombre_cien": "Pinus douglasiana",
            "tamanio": "Grande",
            "municipios_conabio": ["Chimaltitán", "Tequila", "Magdalena", "San Juanito de Escobedo", "Etzatlán", "Ameca", "Guachinango", "San Sebastian del Oeste", "Cabo Corrientes", "Talpa de Allende", "Mascota", "Mixtlán", "Atenguillo", "Cuautlitlán de García Barragán", "Atengo", "Tecolotlán", "Tenamaxtlán", "Ayutla", "Union de Tula", "Villa Purificación", "Cuautitlán de García Barragán", "Tolimán", "Zapotitlán de Vadillo", "Autlán de Navarro", "San Gabriel", "Tonila", "Tuxpan", "Pihuamo", "Tealitlán", "Zapotiltic", "Tamazula de Gordiano", "Gómez Farías", "Zapotlán el Grande", "Atoyac", "Mazamitla", "Valle de Juárez", "Quitupan", "Santa María del Oro", "La Manzanilla de la Paz", "Tapalpa", "Chiquilistlán", "Atemajac de Brizuela", "Tecolotlán", "Unión de Tula"],
            "regiones_koppen": ['CWB'],
            "clorofila": 1
        },
        {
            "nombre_comun":"Pinus escobetón",
            "nombre_cien": "Pinus devoniana",
            "tamanio": "Mediano",
            "municipios_conabio": ["Chimatitlán", "San Martín de Bolaños", "Totatiche", "San Diego de Alejandría", "Acatic", "Arandas", "Jesús María", "San Ignacio Cerro Gordo", "San Julían", "Tepatitlán de Morelos", "Atotonilco el Alto", "Ayotlán", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Concepción de Buenos Aires", "Jocotepec", "La Manzanilla de la Paz", "Mazamitla", "Quitupan", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Valle de Juárez", "Jilotlan de los Dolores", "Pihuamo", "San Gabriel", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Atengo", "Autlán de Navarro", "Ayutla", "Chiquilistlán", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Atemajac de Brizuela", "Cocula", "San Martín Hidalgo", "Tapalpa", "Techaluta de Montenegro", "Villa Corona", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWB'],
            "clorofila": 0
        },
        {
            "nombre_comun":"Primavera",
            "nombre_cien": "Tabebuia Donnell-Smithii",
            "tamanio": "Grande",
            "municipios_conabio": ["Guachinango", "San Sebastián del Oeste", "Puerto Vallarta", "Mascota", "Talpa de Allende", "Tomatlán", "Cabo Corrientes", "Talpa de Allende", "Tomatlán", "Villa Purificación", "La Huerta", "Cihuatlán", "Cuautitlán de García Barragán", "Casimiro Castillo", "Autlán de Navarro", "Tolimán", "Tuxcuacuesco", "Pihuamo", "Jilotlán de los Dolores", "Santa María del Oro", "Tamazula de Gordiano", "Zapotiltic", "Zapotlán el Grande", "Tuxpan", "Tonila", "Sayula", "Zacoalco de Torres", "Acatlán de Juárez", "Villa Corona", "Cocula", "San Martín Hidalgo", "Ameca", "Teuchitlán", "Guadalajara", "Zapopan", "Tlaquepaque", "Tlajomulco de Zúñiga", "Tonalá"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0
        },
        {
            "nombre_comun":"Zarcillo",
            "nombre_cien": "Alvaradoa amorphoides",
            "tamanio": "Pequeño",
            "municipios_conabio": ["Bolaños", "San Martín de Bolaños", "Acatic", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Santa María del Oro", "Jilotlan de los Dolores", "Pihuamo", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Atengo", "Autlán de Navarro", "Chiquilistlán", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Cihuatlán", "Cuautitlán de García Barragán", "La Huerta", "Tomatlán ", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Cocula", "San Martín Hidalgo", "Villa Corona", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 45.6
        }
    ]
    
    tamanio = dict["tamanio"]
    municipio = dict["municipio"]

    arboles_compatibles = []
    txt_arboles = ""
    
    for arbol in ARBOLES_JAL:
        if arbol["tamanio"] == tamanio and municipio in arbol["municipios_conabio"]:
            arboles_compatibles.append(arbol) 
            

    arboles_compatibles.sort(key=lambda p: p["clorofila"], reverse=True)

    arbol_principal = arboles_compatibles[0]

    del arbol_principal["municipios_conabio"]
    del arbol_principal["regiones_koppen"]
    
    for arbol in arboles_compatibles[1:]:
        txt_arboles = txt_arboles + "{} ({})".format(arbol["nombre_comun"],arbol["nombre_cien"]) + "\n"

    return { 'principal': arbol_principal, 'secundarios': txt_arboles }


mensaje = main({"tamanio": "Pequeño", "municipio": "Guadalajara"})
print(mensaje)


