def obtener_animal(letra):
    # Diccionario con animales y sus nombres
    animales = {
        'A': 'Águila',
        'B': 'Ballena',
        'C': 'Caballo',
        'D': 'Delfín',
        'E': 'Elefante',
        'F': 'Foca',
        'G': 'Gorila',
        'H': 'Halcón',
        'I': 'Iguana',
        'J': 'Jirafa',
        'K': 'Koala',
        'L': 'León',
        'M': 'Mono',
        'N': 'Nutria',
        'O': 'Ornitorrinco',
        'P': 'Puma',
        'Q': 'Quokka',
        'R': 'Rinoceronte',
        'S': 'Serpiente',
        'T': 'Tigre',
        'U': 'Urraca',
        'V': 'Vaca',
        'W': 'Wombat',
        'X': 'Xenopus',
        'Y': 'Yak',
        'Z': 'Zorro'
    }
    
    # Convertir la letra ingresada a mayúscula
    letra = letra.upper()
    
    if letra in animales:
        return animales[letra]
    else:
        return "No se encontró ningún animal con esa letra."

# Solicitar al usuario ingresar una letra
letra_usuario = input("Ingrese una letra: ")

# Obtener el animal correspondiente
animal_resultado = obtener_animal(letra_usuario)

# Mostrar el resultado
print(animal_resultado)
#Paula_Palomino
#animales
#IEM_ESCUELA_NORMAL_PASTO
#11-1
