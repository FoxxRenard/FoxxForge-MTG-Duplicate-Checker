import re
from collections import Counter

# Lista de tierras básicas (Commander importante)
basicas = {
    "Plains", "Island", "Swamp", "Mountain", "Forest"
}

def limpiar_lista(texto):
    cartas = []

    for linea in texto.split("\n"):
        linea = linea.strip()

        if not linea:
            continue

        # Ignorar secciones
        if linea.lower() in ["commander", "deck", "sideboard", "maybeboard"]:
            continue

        match = re.match(r"^\d+\s+(.+)$", linea)
        if match:
            carta = match.group(1).strip()

            # Ignorar básicas
            if carta in basicas:
                continue

            cartas.append(carta)

    return cartas


# 🔽 PEGÁ TUS DECKLIST ACÁ 🔽 "EN MOXFIELD EXPORTAR COMO TEXTO PLANO Y PEGAR"
mazos = """

"""

cartas = limpiar_lista(mazos)

conteo = Counter(cartas)

print("\n📋 Lista estilo Moxfield:\n")

for carta, cantidad in sorted(conteo.items()):
    if cantidad > 1:
        print(f"{cantidad} {carta}")