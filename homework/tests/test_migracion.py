import os

def test_migracion():
    # 1. Comprueba que existe el archivo de salida
    if not os.path.exists("data/output/results.tsv"):
        raise FileNotFoundError("El archivo results.tsv no existe en data/output")
    
    result = {}
    # 2. Léelo y construye el diccionario
    with open("data/output/results.tsv", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split("\t")
            result[key] = int(value)

    # 3. Comprueba valores esperados (dentro de la función)
    assert result.get("computational", 0)" == "3"
    assert result.get("analytics", 0) == "5"
