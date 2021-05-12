def main(dict):

    ARBOLES_JAL = [
        {
            "nombre_comun": "Aceitunilla",
            "nombre_cien": "Forestiera tomentosa",
            "tamanio": "Pequeño",
            "municipios_conabio": [],
            "regiones_koppen": ['CWA'],
            "clorofila": 0,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_198715e94f754dbe8129d8d28b22e39c~mv2.jpg"
            
        },
        {
            "nombre_comun":"Anona de la costa",
            "nombre_cien": "Annona reticulata",
            "tamanio": "Mediano",
            "municipios_conabio": ["Mascota", "Puerto Vallarta", "Cabo Corrientes", "Tomatlán", "Talpa de Allende", "Atenguillo", "Villa Purificación", "Autlán de Navarro", "Casimiro Castillo", "La Huerta", "Cihuatlán", "Cuautitlán de García Barragán", "Tolimán", "Tuxcuacuesco", "El Grullo", "El Limón", "Ejutla", "Tonaya", "Zapotitlán de Vadillo", "Tuxpan", "Tonila", "Pihaumo", "Zapoltitic", "Jilotlán de los Dolores", "Santa María del Oro", "Valle de Juárez", "Tamazula de Gordiano", "Poncitlán", "Chapala", "Jamay", "Ocotlán", "La Barca", "Zapotlán del Rey", "Ixtlahuacán de los Membrillos", "Tlajomulco de Zúñiga", "Villa Corona", "Cocula", "Atenguillo", "Atengo", "Tenamaxtlán", "Unión de Tula"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_02704d3cf0634108b4abca57361ed53d~mv2.jpg"
        },
        {
            "nombre_comun":"Arrayán",
            "nombre_cien": "Psidium satorianum",
            "tamanio": "Pequeño",
            "municipios_conabio": ["San Martín de Bolaños"", ""Atotonilco el Alto", "Ayotlán", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Jocotepec", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Jilotlan de los Dolores", "Pihuamo", "San Gabriel", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Zapotlán el Grande", "Atengo", "Autlán de Navarro", "Ayutla", "Chiquilistlán", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Cihuatlán", "Cuautitlán de García Barragán", "La Huerta", "Tomatlán ", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Teuchitlán", "Acatlán de Juárez", "Amacueca", "Atemajac de Brizuela", "Cocula", "San Martín Hidalgo", "Sayula", "Tapalpa", "Techaluta de Montenegro", "Teocuitatlán de Corona", "Villa Corona", "Zacoalco de Torres", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_81d61a2de29548c6b39136bdb789c9bd~mv2.jpg"
        },
        {
            "nombre_comun":"Ceiba",
            "nombre_cien": "Ceiba pentandra",
            "tamanio": "Grande",
            "municipios_conabio": ["Puerto Vallarta", "San Sebastían del Oeste", "Cabo Corrientes", "Tomatlán", "Villa Purificación", "La Huerta", "Casimiro Castillo", "Cihuatlán", "Tolimán", "Tuxpan", "Pihuamo", "Tuxcacuesco", "El Grullo", "El Limón", "Ejutla", "Tonaya", "Juchitlán", "Tenamaxtlán", "San Juanito de Escobedo", "Amatitán", "Teuchitlán", "Ahualulco de Mercado", "Zapotiltic", "Zapotlán el Grande"],
            "regiones_koppen": [],
            "clorofila": 37.7,
            "imagen_url": ""
        },
        {
            "nombre_comun":"Cedro Blanco",
            "nombre_cien": "Cupressus lusitanica",
            "tamanio": "Grande",
            "municipios_conabio": [],
            "regiones_koppen": [],
            "clorofila": 45.3,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_505afcd7f2d040bb8390939a655f2c4b~mv2.jpg"
        },
        {
            "nombre_comun":"Cedro Rojo",
            "nombre_cien": "Cedrela odorata",
            "tamanio": "Grande",
            "municipios_conabio": ["Unión de San Antonio", "San Diego de Alejandría", "San Julián", "Lagos de Moreno", "Arandas", "Jesús María", "Degollado", "Atotonilco el Alto", "Tepatitlán de Morelos", "San Ignacio Cerro Gordo", "San Miguel el Alto", "Acatic", "Zapotlanejo", "Juanacatlán", "Poncitlán", "Chapala", "Jocotepec", "Tuxcueca", "Tizapán el Alto", "Tlajomulco de Zúñiga", "Zacoalco de Torres", "Villa Corona", "Cocula", "Quitupan", "Valle de Juárez", "Mazamitla", "La Manzanilla de la Paz", "Concepción de Buenos Aires", "Atoyac", "Gómez Farías", "Atemajac de Brizuela", "Tecolotlán", "Tenamaxtlán", "Juchitlán", "Chiquilistlán", "Tapalpa", "San Gabriel"],
            "regiones_koppen": ['CWA', 'CWB'],
            "clorofila": 33.5,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_fd0ba7fa974f476d9976ea8be0291573~mv2.jpg"
        },
        {
            "nombre_comun":"Fresno",
            "nombre_cien": "Fraxinus uhdei",
            "tamanio": "Grande",
            "municipios_conabio": [],
            "regiones_koppen": [],
            "clorofila": 32.7,
            "imagen_url": ""
        },

        {
            "nombre_comun":"Guamúchil",
            "nombre_cien": "Pithecellobim dulce",
            "tamanio": "Grande",
            "municipios_conabio": ["Bolaños", "Chimatitlan", "Colotlán", "Huejúcar", "Huejuquilla el Alto", "Mezquitic", "San Martín de Bolaños", "Santa María de los Ángeles", "Totatiche", "Villa Guerrero", "Encarnacion de Diaz", "Lagos de Moreno", "San Diego de Alejandría", "San Juan de los Lagos", "Union de San Antonio ", "Villa Hidalgo", "Acatic", "Arandas", "Cañadas de Obregón", "Jalostotitlán", "Jesús María", "Mexticacan", "San Ignacio Cerro Gordo", "San Julían", "San Miguel el Alto", "Tepatitlán de Morelos", "Valle de Guadalupe", "Yahualica de Connzález Gallo", "Atotonilco el Alto", "Ayotlán", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Concepción de Buenos Aires", "Jocotepec", "La Manzanilla de la Paz", "Mazamitla", "Quitupan", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Valle de Juárez", "Gómez Farias", "Jilotlan de los Dolores", "Pihuamo", "San Gabriel", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Zapotlán el Grande", "Atengo", "Autlán de Navarro", "Ayutla", "Chiquilistlán", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Cihuatlán", "Cuautitlán de García Barragán", "La Huerta", "Tomatlán ", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Amacueca", "Atemajac de Brizuela", "Atoyac", "Cocula", "San Martín Hidalgo", "Sayula", "Tapalpa", "Techaluta de Montenegro", "Teocuitatlán de Corona", "Villa Corona", "Zacoalco de Torres", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'BSH', 'AW'], 
            "clorofila": 41.9,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_5d365cb5fd1f40cc8c13d31c7a67af92~mv2.jpg"
        },
        {
            "nombre_comun":"Guayabo",
            "nombre_cien": "Psidium guajava",
            "tamanio": "Pequeño",
            "municipios_conabio": ["Bolaños", "Chimatitlan", "Colotlán", "Huejúcar", "Huejuquilla el Alto", "Mezquitic", "San Martín de Bolaños", "Santa María de los Ángeles", "Totatiche", "Villa Guerrero", "Encarnacion de Diaz", "Lagos de Moreno", "San Diego de Alejandría", "San Juan de los Lagos", "Union de San Antonio ", "Villa Hidalgo", "Acatic", "Arandas", "Cañadas de Obregón", "Jalostotitlán", "Jesús María", "Mexticacan", "San Ignacio Cerro Gordo", "San Julían", "San Miguel el Alto", "Tepatitlán de Morelos", "Valle de Guadalupe", "Yahualica de Connzález Gallo", "Atotonilco el Alto", "Ayotlán", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Concepción de Buenos Aires", "Jocotepec", "La Manzanilla de la Paz", "Mazamitla", "Quitupan", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Valle de Juárez", "Gómez Farias", "Jilotlan de los Dolores", "Pihuamo", "San Gabriel", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Zapotlán el Grande", "Atengo", "Autlán de Navarro", "Ayutla", "Chiquilistlán", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Cihuatlán", "Cuautitlán de García Barragán", "La Huerta", "Tomatlán ", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Amacueca", "Atemajac de Brizuela", "Atoyac", "Cocula", "San Martín Hidalgo", "Sayula", "Tapalpa", "Techaluta de Montenegro", "Teocuitatlán de Corona", "Villa Corona", "Zacoalco de Torres", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 36.9,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_0196cd419e894d6588772f4226b5dc57~mv2.jpg"
        },
        {
            "nombre_comun":"Jacaranda",
            "nombre_cien": "Jacaranda mimosifolia",
            "tamanio": "Mediano",
            "municipios_conabio": [],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 36.4,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_3a8e983dff0148c0b292f2f840e7d6f0~mv2.jpg"
        },
        {
            "nombre_comun":"Jinuicil Peludo",
            "nombre_cien": "Inga vera",
            "tamanio": "Mediano",
            "municipios_conabio": [],
            "regiones_koppen": ['AW'],
            "clorofila": 43.2,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_3a8e983dff0148c0b292f2f840e7d6f0~mv2.jpg"
        },
        {
            "nombre_comun":"Palmilla",
            "nombre_cien": "Podocarpus matudae",
            "tamanio": "Grande",
            "municipios_conabio": [],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_85a02f354edf4dfa886f94a91654b412~mv2.jpg"
        },
        {
            "nombre_comun":"Papelillo",
            "nombre_cien": "Bursera multijuga",
            "tamanio": "Pequeño",
            "municipios_conabio": ["Bolaños", "Chimatitlan", "Colotlán", "Huejúcar", "Huejuquilla el Alto", "Mezquitic", "San Martín de Bolaños", "Santa María de los Ángeles", "Totatiche", "Villa Guerrero", "San Diego de Alejandría", "San Juan de los Lagos", "Teocaltiche", "Union de San Antonio ", "Villa Hidalgo", "Acatic", "Arandas", "Cañadas de Obregón", "Jalostotitlán", "Jesús María", "Mexticacan", "San Ignacio Cerro Gordo", "San Julían", "San Miguel el Alto", "Tepatitlán de Morelos", "Valle de Guadalupe", "Yahualica de Connzález Gallo", "Atotonilco el Alto", "Ayotlán", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Concepción de Buenos Aires", "Jocotepec", "La Manzanilla de la Paz", "Mazamitla", "Quitupan", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Valle de Juárez", "Gómez Farias", "Jilotlan de los Dolores", "Pihuamo", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Zapotlán el Grande", "Atengo", "Autlán de Navarro", "Ayutla", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Amacueca", "Atoyac", "Cocula", "San Martín Hidalgo", "Sayula", "Techaluta de Montenegro", "Teocuitatlán de Corona", "Villa Corona", "Zacoalco de Torres", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_cedd0f88eeed4247bf6355a54198c616~mv2.jpg"
        },
        {
            "nombre_comun":"Pino albellano",
            "nombre_cien": "Pinus douglasiana",
            "tamanio": "Grande",
            "municipios_conabio": ["Chimaltitán", "Tequila", "Magdalena", "San Juanito de Escobedo", "Etzatlán", "Ameca", "Guachinango", "San Sebastian del Oeste", "Cabo Corrientes", "Talpa de Allende", "Mascota", "Mixtlán", "Atenguillo", "Cuautlitlán de García Barragán", "Atengo", "Tecolotlán", "Tenamaxtlán", "Ayutla", "Union de Tula", "Villa Purificación", "Cuautitlán de García Barragán", "Tolimán", "Zapotitlán de Vadillo", "Autlán de Navarro", "San Gabriel", "Tonila", "Tuxpan", "Pihuamo", "Tealitlán", "Zapotiltic", "Tamazula de Gordiano", "Gómez Farías", "Zapotlán el Grande", "Atoyac", "Mazamitla", "Valle de Juárez", "Quitupan", "Santa María del Oro", "La Manzanilla de la Paz", "Tapalpa", "Chiquilistlán", "Atemajac de Brizuela", "Tecolotlán", "Unión de Tula"],
            "regiones_koppen": ['CWB'],
            "clorofila": 0,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_c5f2a9d820304df3ba94f69b78a7028f~mv2.jpg"
        },
        {
            "nombre_comun":"Pinus escobetón",
            "nombre_cien": "Pinus devoniana",
            "tamanio": "Grande",
            "municipios_conabio": ["Chimatitlán", "San Martín de Bolaños", "Totatiche", "San Diego de Alejandría", "Acatic", "Arandas", "Jesús María", "San Ignacio Cerro Gordo", "San Julían", "Tepatitlán de Morelos", "Atotonilco el Alto", "Ayotlán", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Concepción de Buenos Aires", "Jocotepec", "La Manzanilla de la Paz", "Mazamitla", "Quitupan", "Santa María del Oro", "Tizapán el Alto", "Tuxcueca", "Valle de Juárez", "Jilotlan de los Dolores", "Pihuamo", "San Gabriel", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Atengo", "Autlán de Navarro", "Ayutla", "Chiquilistlán", "Cuautla", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Cabo Corrientes", "Guachinango", "Mascota", "Mixtlán", "Atenguillo", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Atemajac de Brizuela", "Cocula", "San Martín Hidalgo", "Tapalpa", "Techaluta de Montenegro", "Villa Corona", "Cuquío", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Ixtlahuacán del Río", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWB'],
            "clorofila": 0,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_50d7204ffe144e9cbb0aada0a6c23894~mv2.jpg"
        },
        {
            "nombre_comun":"Primavera",
            "nombre_cien": "Tabebuia Donnell-Smithii",
            "tamanio": "Grande",
            "municipios_conabio": ["Guachinango", "San Sebastián del Oeste", "Puerto Vallarta", "Mascota", "Talpa de Allende", "Tomatlán", "Cabo Corrientes", "Talpa de Allende", "Tomatlán", "Villa Purificación", "La Huerta", "Cihuatlán", "Cuautitlán de García Barragán", "Casimiro Castillo", "Autlán de Navarro", "Tolimán", "Tuxcuacuesco", "Pihuamo", "Jilotlán de los Dolores", "Santa María del Oro", "Tamazula de Gordiano", "Zapotiltic", "Zapotlán el Grande", "Tuxpan", "Tonila", "Sayula", "Zacoalco de Torres", "Acatlán de Juárez", "Villa Corona", "Cocula", "San Martín Hidalgo", "Ameca", "Teuchitlán", "Guadalajara", "Zapopan", "Tlaquepaque", "Tlajomulco de Zúñiga", "Tonalá"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 0,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_7a6c3fb70e334594b8e3e71865998b65~mv2.jpg"
        },
        {
            "nombre_comun":"Zarcillo",
            "nombre_cien": "Alvaradoa amorphoides",
            "tamanio": "Pequeño",
            "municipios_conabio": ["Bolaños", "San Martín de Bolaños", "Acatic", "Degollado", "Jamay", "La Barca", "Ocotlán", "Poncitlán", "Tototlán", "Zapotlán del Rey", "Chapala", "Santa María del Oro", "Jilotlan de los Dolores", "Pihuamo", "Tamazula de Gordiano", "Tecalitlán", "Tolimán", "Tonila", "Tuxpan", "Zapotiltic", "Zapotitlán de Vadillo", "Atengo", "Autlán de Navarro", "Chiquilistlán", "Ejutla", "El Grullo", "El Limón", "Juchitlán", "Tecolotlán", "Tenamaxtlán", "Tonaya", "Tuxcacuesco", "Union de Tula", "Casimiro Castillo", "Cihuatlán", "Cuautitlán de García Barragán", "La Huerta", "Tomatlán ", "Villa Putificación", "Puerto Vallarta", "Cabo Corrientes", "Guachinango", "San Sebastián del Oeste", "Talpa de Allende", "Ahualulco de Mercado", "Amatitán", "Ameca", "El Arenal", "Etzatlán", "Hostotipaquillo", "Magdalena", "San Juanito de Escobedo", "San Marcos", "Tala", "Tequila", "Teuchitlán", "Acatlán de Juárez", "Cocula", "San Martín Hidalgo", "Villa Corona", "El Salto", "Guadalajara", "Ixtlahuacán de los Membrillos", "Juanacatlán", "San Cristóbal de la Barranca", "Tlaquepaque", "Tlajomulco", "Tonalá", "Zapopan", "Zapotlanejo"],
            "regiones_koppen": ['CWA', 'AW'],
            "clorofila": 45.6,
            "imagen_url": "https://static.wixstatic.com/media/e887b4_cb957f930cf34dd6b43d0d8985185846~mv2.jpg"
        }
    ]

    KOPPEN = {
        "Guadalajara": "CWA", "Cuquío": "CWB", "El Salto": "CWA", "Ixtlahuacán de los Membrillos": "CWA", "Ixtlahuacán del Río": "CWA", "Juanacatlán": "CWA", "San Cristóbal de la Barranca": "AW", "Tlaquepaque": "CWA", "Tlajomulco": "CWA", "Tonalá": "CWA", "Zapopan": "CWA", "Zapotlanejo": "CWA", "Zacoalco de Torres": "BSH", "Villa Corona": "CWA", "Teocuitatlán de Corona": "BSH", "Techaluta de Montenegro": "BSH", "Tapalpa": "CWB", "Sayula": "CWA", "San Martín de Hidalgo": "CWA", "Cocula": "CWA", "Atoyac": "BSH",  "Atemajac de Brizuela": "CWB", "Amecua": "BSH", "Acatlan de Juarez": "CWA", "Teuchitlan": "CWA", "Tequila": "AW", "Tala": "CWA", "San Marcos": "CWA", "San Juanito de Escobedo": "CWA", "Magdalena": "CWA", "Hostotipaquillo": "CWA", "Etzatlán": "CWA", "El Arenal": "CWA", "Ameca": "CWA", "Amatitán": "CWA", "Ahualulco de Mercado": "CWA", "Talpa de Allende": "CWA", "San Sebastián del Oeste": "CWB", "Atenguillo": "CWA", "Mixtlán": "CWB", "Mascota": "CWA", "Guachinango": "CWA", "Cabo Corrientes": "AW","Puerto Vallarta": "AW", "Villa Putificación": "AW", "Tomatlán": "AW", "La Huerta": "AW", "Cuautitlán de García Barragán": "AW",  "Cihuatlán": "AW", "Casimiro Castillo": "AW", "Union de Tula": "AW", "Tuxcacuesco": "AW", "Tonaya": "BSH", "Tenamaxtlán": "CWA", "Tecolotlán": "AW", "Juchitlán": "BSH", "El Limón": "CWA", "El Grullo": "AW", "Ejutla": "AW", "Cuautla": "CWB", "Chiquilistlán": "CWB", "Ayutla": "CWA", "Autlán de Navarro": "AW", "Atengo": "CWA", "Zapotlán el Grande": "BSH", "Zapotitlan de Vadillo": "AW", "Zapotiltic": "CWA", "Tuxpan": "AW", "Tonila": "AW", "Tolimán": "BSH", "Tecalitlán": "AW", "Tamazula de Gordiano": "AW", "San Gabriel": "AW", "Pihuamo": "AW", "Jilotlán de los Dolores": "AW", "Gómez Farias": "AW", "Valle de Juarez": "CWB", "Tuxcuecan": "CWA", "Tizapán del Alto": "CWA", "Santa María del Oro": "CWA", "Quitupan": "CWB", "Mazamitla": "CWB", "La manzanilla de la Paz": "CWB", "Jocotepec": "CWA", "Concepción de Buenos Aires": "CWB", "Chapala": "CWA", "Zapotlán del Rey": "CWA", "Tototlán": "CWA", "Poncitlán": "CWA", "Ocotlán": "CWA", "La Barca": "CWA", "Jamay": "CWA", "Degolaldo": "CWA", "Ayotlán": "CWA", "Atotonilco el Alto": "CWA", "Yahulica de Gonzáles Gallo": "CWB", "Valle de Guadalupe": "CWA", "Tepatitlán de Morelos": "CWA", "San Miguel el Alto": "CWB", "San Julian": "CWB", "San Ignacio Cerro Gordo": "CWB", "Mexticacan": "CWA", "Jesús Maria": "CWB", "Jalostotitlán": "CWA", "Cañadas de Obregón": "BSH", "Arandas": "CWB", "Acatic": "CWB", "Villa Hidalgo": "BSH", "Union de San Antonio": "CWA", "Teocaltiche": "BSH", "San Juan de los Lagos": "CWA", "San Diego de Alejandría": "CWA", "Ojuelos de Jalisco": "BSK", "Lagos de Moreno": "BSH", "Encarnación de Diaz": "BSH", "Villa Guerrero": "CWA", "Totatiche": "CWA", "Santa María de los ängeles": "CWA", "San Martín de Bolaños": "BSH", "Mezquitic": "BSH",
        "Huejuquilla el Ato": "CWA", "Huejúcar": "BSH", "Colotlán": "BSH", "Chimatitlán": "BSH", "Bolaños": "BSH"
    }
    
    KOPPEN = {
        "Guadalajara": "CWA"
    }

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


mensaje = main({"tamanio": "Pequeño", "municipio": "Guadalajara"})
print(mensaje)
