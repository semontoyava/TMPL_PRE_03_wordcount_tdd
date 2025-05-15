import sys
from ._internals.read_all_lines   import read_all_lines
from ._internals.preprocess_lines import preprocess_lines
from ._internals.split_into_words import split_into_words
from ._internals.count_words      import count_words
from ._internals.write_word_counts import write_word_counts

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder, output_folder = sys.argv[1], sys.argv[2]
    lines   = read_all_lines(input_folder)
    clean   = preprocess_lines(lines)
    words   = split_into_words(clean)
    counter = count_words(words)
    write_word_counts(counter, output_folder)

if __name__ == "__main__":
    main()
