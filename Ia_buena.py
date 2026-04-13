import Coneccion_IA
from Coneccion_IA import info_manga_personajes, info_manga_capitulos, conexion_ia_epikarda, respuesta_de_llama
print("ya casi queda")
modelo_carbon = conexion_ia_epikarda()
print("di un nombre o algo xd")

while True:
    print("\n" + "="*40)
    nombre_buscado = input("¿A qué personaje buscas? (o escribe 'chao chao'): ")
    if nombre_buscado.lower() == "chao chao":
        print("¡Hasta la próxima!")
        break
    info_personaje = Coneccion_IA.info_manga_personajes(nombre_buscado)
        #se busca el personaje

    if info_personaje:
        print(f"ahí tan los datos de personaje encontrados: {info_personaje['nombre']}")
        num_cap = input(f"¿Sobre qué número de capítulo quieres que {info_personaje['nombre']} sea experta?: ")
        info_capitulo = Coneccion_IA.info_manga_capitulos(num_cap)
        #busca el capitulo pero aun no se como hacer que sea automático
        if info_capitulo:
            print(f"apenas está cargando el {num_cap} ")
            print("Vete a tomar un café, esto va para largo...")

            pregunta_user = input(f"Pregúntale algo a {info_personaje['nombre']}: ")
            # se pasan los datos
            respuesta_final = Coneccion_IA.respuesta_de_llama(
                info_personaje, 
                info_capitulo, 
                pregunta_user, 
                modelo_carbon
            )
            print("\nFinalmente ya tienes la respuesta:")
            print(f"[{info_personaje['nombre']}]: {respuesta_final}")
        else:
            print(f"El capítulo {num_cap} no está en la base")
    else:
        print(f"No encontré a '{nombre_buscado}' en la base")
        #no se que hice, pero funciona de milagro