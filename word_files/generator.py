import os
import random

def generar_textos_español(
    num_files=100,
    min_words=90_000,
    max_words=100_000,
    word_list_path="spanish_words.info"
):
    """
    Genera num_files archivos de texto (file_01.txt … file_100.txt)
    en el mismo directorio que este script, cada uno con entre
    min_words y max_words palabras en español, usando como vocabulario
    el archivo word_list_path (una palabra por línea).
    """
    # Carpeta donde está este script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Ruta al vocabulario
    vocab_path = os.path.join(script_dir, word_list_path)
    with open(vocab_path, "r", encoding="utf-8") as f:
        vocab = [w.strip() for w in f if w.strip()]
    if not vocab:
        raise RuntimeError("El archivo de vocabulario está vacío.")

    # Generar los archivos directamente en script_dir
    for i in range(1, num_files + 1):
        count = random.randint(min_words, max_words)
        palabras = random.choices(vocab, k=count)
        filename = f"file_{i:02d}.txt"
        path = os.path.join(script_dir, filename)
        with open(path, "w", encoding="utf-8") as f_out:
            f_out.write(" ".join(palabras))
        print(f"Creado {filename} con {count} palabras")

if __name__ == "__main__":
    generar_textos_español()
