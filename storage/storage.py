import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
ARQUIVO = os.path.join(DATA_DIR, "carros.json")

def carregar_carros():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_carros(carros):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(carros, f, ensure_ascii=False, indent=4)


def gerar_novo_id():
    carros = carregar_carros()
    if not carros:
        return 1
    return max(c["id"] for c in carros) + 1

