"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: [Sara Romero Peralta]
Fecha: [06/11/2025]
"""


def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra() -> str:
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns:
        str: La palabra a adivinar en mayúsculas
    """
    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la palabra sea válida
    # - Verificar que tenga al menos 5 caracteres (len())
    # - Verificar que solo contenga letras (isalpha())
    # - Convertir a mayúsculas (upper())
    valido = False
    while valido == False:
        palabra = input("Jugador 1: Introduce la palabra a adivinar (mínimo 5 letras):")
        if len(palabra) < 5:
            print("Error: La palabra debe tener al menos 5 caracteres.")
        elif not palabra.isalpha():
            print("Error: La palabra solo puede contener letras.")
        else:
            valido = True
    
    return palabra.upper()


def solicitar_letra(letras_usadas:list) -> str:
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
    """
    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la letra sea válida
    # - Verificar que sea solo un carácter (len() == 1)
    # - Verificar que sea una letra (isalpha())
    # - Verificar que no esté en letras_usadas (operador 'in')
    # - Convertir a mayúsculas (upper())
    valida = False
    while valida == False:
        letra=input("Introduce una letra: ")
        if len(letra) != 1 or not letra.isalpha():
            print("Error: Debe ser una letra")
        elif letra in letras_usadas:
            print("Error: Ya has usado esa letra")
        else:
            letras_usadas.append(letra)
            return letra.upper()
    


def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """
    # TODO: Implementar la función
    # - Imprimir intentos restantes
    # - Imprimir la palabra con espacios entre caracteres
    # - Imprimir las letras usadas
    print(f"Intentos restantes: {intentos}\n")

    print("Palabra: \n")
    for c in palabra_oculta:
        print(c, end =" ")
    
    print("Letras usadas:\n")
    for c in letras_usadas:
        if c == letras_usadas[-1]:
            print(c)
        else:
            print(c, end =" ")

def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Args:
        palabra (str): La palabra completa a adivinar
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
        
    Returns:
        str: La palabra oculta actualizada
    """
    # TODO: Implementar la función
    # - Recorrer la palabra original con un bucle for
    # - Usar enumerate() para obtener índice y carácter
    # - Si el carácter coincide con la letra, reemplazar en palabra_oculta
    # - Puedes convertir palabra_oculta a lista, modificar y volver a string
    lista_palabra_oculta = list(palabra_oculta)
    for c, letra_temporal in enumerate(palabra):
        if letra == letra_temporal:
            lista_palabra_oculta[c] = letra
    
    palabra_oculta_nueva = ""
    for i in lista_palabra_oculta:
        palabra_oculta_nueva = palabra_oculta_nueva + i
    
    return palabra_oculta_nueva


def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    
    # TODO: Solicitar la palabra al jugador 1
    # palabra = solicitar_palabra()
    palabra = solicitar_palabra()
    # TODO: Limpiar la pantalla para que el jugador 2 no vea la palabra
    # limpiar_pantalla()
    limpiar_pantalla()
    palabra_oculta= ""
    for i in palabra:
        palabra_oculta = palabra_oculta + "_"
    
    # TODO: Inicializar variables del juego
    # - palabra_oculta: string con guiones bajos (ej: "_ _ _ _ _")
    # - intentos: número de intentos restantes
    # - letras_usadas: lista vacía
    # - juego_terminado: False

    letras_usadas = []
    intentos = INTENTOS_MAXIMOS
    juego_terminado = False
    
    print("Jugador 2: ¡Adivina la palabra!\n")
    
    # TODO: Bucle principal del juego
    # - Mientras haya intentos y el juego no haya terminado:
    #   1. Mostrar el estado actual
    #   2. Solicitar una letra
    #   3. Añadir la letra a letras_usadas
    #   4. Si la letra está en la palabra:
    #      - Actualizar palabra_oculta
    #      - Mostrar mensaje de acierto
    #      - Si ya no hay '_' en palabra_oculta, el jugador ha ganado
    #   5. Si la letra NO está en la palabra:
    #      - Restar un intento
    #      - Mostrar mensaje de fallo
    while not juego_terminado and intentos > 0:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        letra = solicitar_letra(letras_usadas)
        if letra in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print(f"¡Bien! La letra {letra} está en la palabra.")
            if not "_" in palabra_oculta:
                print(f"¡FELICIDADES! Has adivinado la palabra: {palabra}")
                juego_terminado = True
        else:
            print("¡Letra incorrecta!")
            intentos = intentos - 1
            if intentos == 0:
                print(f"¡GAME OVER! Te has quedado sin intentos.\n La palabra era: {palabra}")


def main():
    """
    Punto de entrada del programa
    """
    # TODO (Opcional): Preguntar si quiere jugar otra vez
    # jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    # if jugar_otra_vez.lower() == 's':
    #     main()
    seguir = True
    while seguir == True:
        jugar()
        valido = False
        while valido == False:
            jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n)")
            if jugar_otra_vez.lower() == "s" or jugar_otra_vez.lower() == "n":
                valido = True
        if jugar_otra_vez == "s":
            jugar()
        else:
            seguir = False
            print("Saliendo del juego...")

    


if __name__ == "__main__":
    main()
