import os

def write_word_counts(counter, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    out_path = os.path.join(output_folder, "results.tsv")
    with open(out_path, "w", encoding="utf-8") as f:
        for word, count in counter.items():
            f.write(f"{word}\t{count}\n")
