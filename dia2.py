# dia2.py - Mejora del gestor de prompts para Vita

import json

def mostrar_prompts(prompts):
    print("=== Mis Prompts para Kuronagi Setsuna ===\n")
    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. {prompt}")
    print(f"\n¡Listo! Total de prompts: {len(prompts)}")

def guardar_prompts(prompts, archivo="prompts.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Prompts guardados en {archivo}")

# Tus prompts (puedes agregar más)
mis_prompts = [
    "Kuronagi Setsuna in elegant black suit, detailed face, soft lighting, anime style",
    "Kuronagi Setsuna holding flowers, gentle expression, fantasy background",
    "Kuronagi Setsuna in modern casual clothes, confident pose, warm colors",
    "1boy, solo, black hair, short hair, serious expression, looking at viewer, black bodysuit, skintight suit, dark clothing, gloves, holding weapon, oversized sword, giant sword, black sword, standing, full body, on cliff, rocky terrain, red sky, red clouds, crimson atmosphere, red moon, apocalyptic scenery, dark fantasy, post-apocalyptic, hellish landscape, dramatic lighting, smoke, fog, glowing sky, high contrast, anime style, detailed background, masterpiece, best quality, cinematic composition, dynamic perspective"
]

# Mostrar
mostrar_prompts(mis_prompts)

# Guardar en archivo
guardar_prompts(mis_prompts)