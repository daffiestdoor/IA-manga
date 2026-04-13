def info_manga_personajes(nombre_a_buscar):
    import sqlite3
    este_es_el_puente= sqlite3.connect("manga_100_kanojo.db")
    #con .connect se conecta el codigo a la base de datos
    mensajero=este_es_el_puente.cursor()
    # con .cursor puedes hacer el SELECT
    mensajero.execute("SELECT * FROM personajes WHERE personaje=?", (nombre_a_buscar,))
    # con .execute se lee lo que está en la variable
    dato= mensajero.fetchone()
    este_es_el_puente.close()
    #con .fetchone se regresa la informacion al codigo especificamente de esa celda
    if dato:
        esta_es_columna_wey = ["nombre", "tipo", "sexo", "debut", "personalidad", "apariencia", "habilidades", "cumple", "frase", "dato_curioso"]
    #con el if creas el paso para un bucle for sabrosongo y la variable cuyo nombre no repetiré xD, ahi guardas los datos
        personaje = {esta_es_columna_wey[indice]: str(dato[indice]).strip() for indice in range(len(esta_es_columna_wey))}
        #este es el bucle for bien sabroso y raro que va al revés, primero los datos y luego el for
        return personaje
        #esa madre devuelve el diccionario
    return None 
    
def info_manga_capitulos(capitulo_a_buscar):
    import sqlite3
    este_es_el_puente= sqlite3.connect("manga_100_kanojo.db")
    mensajero= este_es_el_puente.cursor()
    mensajero.execute("SELECT * FROM capitulos WHERE capitulo=?", (capitulo_a_buscar,))
    dato2= mensajero.fetchone()
    este_es_el_puente.close()
    if dato2:
        otra_columna = ["capitulo", "título", "presencia", "evento_clave", "resumen"]
        capitulo = {otra_columna[indice2]: str(dato2[indice2]).strip() for indice2 in range(len(otra_columna))}
        return capitulo
    return None 
    
def conexion_ia_epikarda():
    from llama_cpp import Llama
    modelo_carbon = Llama ( model_path= "modelo_llama.gguf", n_ctx= 512, n_threads = 3, n_batch=128, verbose = False )
    return modelo_carbon
    #n_ctx es la memoria a corto plazo, me puse un shingo; n_threads son los nucleos que usará este cel verbose es pa ver solo el resultao, no el proceso y pa q no se me llene el cel de kk (ahora uso laptop pero dejaré eso así)

def respuesta_de_llama(datos_personaje, datos_capitulo, pregunta_usuario, modelo_IA):
    # 1. El System Prompt define quién es Y qué sabe
    system_prompt = f"""
    You are {datos_personaje['nombre']} from the manga '100 Kanojo'.
    PERSONALITY: {datos_personaje['personalidad']}.
    KNOWLEDGE BASE: You are an expert on the manga chapters. 
    Use the following data to answer: "{datos_capitulo['resumen']}" and "{datos_capitulo['evento_clave']}".
    INSTRUCTION: Respond as {datos_personaje['nombre']} would, using your personality and typical phrases, 
    but ensure your answer is based on the provided manga facts. Stay friendly and in character.
    Always respond in Spanish.
    """
    output = modelo_IA.create_chat_completion(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": pregunta_usuario}
        ],
        max_tokens=150, # el espacio o los caracteres que usa
        temperature=0.7, # según es la amabilidad, creo
        repeat_penalty=1.2
    )
    return output['choices'][0]['message']['content']