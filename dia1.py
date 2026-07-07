# dia1.py - Mi primer ejercicio de Functions + Prompts para Vita

def mostrar_prompts(prompts):
    """Función que recibe una lista de prompts y los imprime bonitos"""
    print("=== Mis Prompts para Kuronagi Setsuna ===\n")
    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. {prompt}")
    print("\n¡Listo! Total de prompts:", len(prompts))

# Lista de ejemplo (puedes cambiar estos prompts por los tuyos)
mis_prompts = [
    "Kuronagi Setsuna in elegant black suit, detailed face, soft lighting, anime style",
    "Kuronagi Setsuna holding flowers, gentle expression, fantasy background",
    "Kuronagi Setsuna in modern casual clothes, confident pose, warm colors"
]

# Llamamos a la función
mostrar_prompts(mis_prompts)