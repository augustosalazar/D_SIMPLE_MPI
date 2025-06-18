import os
from collections import Counter
import time

def topN_palabras_file1_en_otros(dir_path, file1_name="file_01.txt", case_sensitive=False, top_n=10):
    """
    Calcula el top N de palabras de file_01.txt según su frecuencia total
    en el resto de archivos .txt dentro de dir_path.
    """
    path1 = os.path.join(dir_path, file1_name)
    if not os.path.isfile(path1):
        raise FileNotFoundError(f"No se encontró '{file1_name}' en '{dir_path}'")

    # Leer y normalizar palabras de file_01.txt
    with open(path1, "r", encoding="utf-8") as f:
        palabras1 = f.read().split()
    if not case_sensitive:
        palabras1 = [w.lower() for w in palabras1]
    palabras_unicas = set(palabras1)

    # Contador global
    freq_global = Counter()

    # Recorre todos los .txt exceptuando file_01.txt
    for fname in os.listdir(dir_path):
        if not fname.lower().endswith(".txt") or fname == file1_name:
            continue
        ruta = os.path.join(dir_path, fname)
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                palabras = linea.split()
                if not case_sensitive:
                    palabras = [w.lower() for w in palabras]
                for w in palabras:
                    if w in palabras_unicas:
                        freq_global[w] += 1

    return freq_global.most_common(top_n)

def main():
    # Parámetros fijos (no se usan opciones por línea de comandos)
    dir_path = os.path.abspath(".")          # Directorio actual
    file1_name = "file_01.txt"                # Archivo base
    case_sensitive = False                   # ¿Distinguir mayúsculas?
    top_n = 10                               # Número de palabras a extraer

    # Medir tiempo de ejecución
    t0 = time.perf_counter()

    try:
        top_words = topN_palabras_file1_en_otros(
            dir_path,
            file1_name=file1_name,
            case_sensitive=case_sensitive,
            top_n=top_n
        )
    except FileNotFoundError as e:
        print("Error:", e)
        return

    t1 = time.perf_counter()
    elapsed = t1 - t0

    # Salida
    print(f"Tiempo de ejecución: {elapsed:.3f} segundos\n")
    print(f"Top {top_n} palabras de {file1_name} según frecuencia en otros archivos:")
    for palabra, cuenta in top_words:
        print(f"  {palabra}: {cuenta}")

if __name__ == "__main__":
    main()
